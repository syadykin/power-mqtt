from machine import UART, Pin

def _hex_to_byte(obj):
    hex_str = ''.join([chr(x) for x in obj])
    return bytes.fromhex(hex_str)

def _get_frame_checksum(frame):

    assert isinstance(frame, bytes)

    sum = 0
    for byte in frame:
        sum += byte
    sum = ~sum
    sum %= 0x10000
    sum += 1

    return sum

def _get_info_length(info):

    assert isinstance(info, bytes)

    len_id = len(info)
    if len_id == 0:
        return 0

    len_id_sum = (len_id & 0xf) + ((len_id >> 4) & 0xf) + ((len_id >> 8) & 0xf)
    len_id_modulo = len_id_sum % 16
    len_id_invert_plus_one = 0b1111 - len_id_modulo + 1

    return (len_id_invert_plus_one << 12) + len_id

def _encode_cmd(address, cid2, info = b''):

    assert isinstance(info, bytes)

    cid1 = 0x46

    info_length = _get_info_length(info)

    frame = "{:02X}{:02X}{:02X}{:02X}{:04X}".format(0x20, address, cid1, cid2, info_length).encode()
    frame += info

    frame_chk_sum = _get_frame_checksum(frame)
    whole_frame = (b"~" + frame + "{:04X}".format(frame_chk_sum).encode() + b"\r")

    return whole_frame

def _decode_hw_frame(raw_frame):

    assert isinstance(raw_frame, bytes)

    frame_data = raw_frame[1:len(raw_frame) - 5]
    frame_chk_sum = raw_frame[len(raw_frame) - 5:-1]

    got_frame_checksum = _get_frame_checksum(frame_data)
    assert got_frame_checksum == int(frame_chk_sum, 16)

    return frame_data

def _decode_frame(frame):

    return {
      'ver': _hex_to_byte(frame[0:2]),
      'adr': _hex_to_byte(frame[2:4]),
      'cid1': _hex_to_byte(frame[4:6]),
      'cid2': _hex_to_byte(frame[6:8]),
      'infolength': _hex_to_byte(frame[8:12]),
      'info': _hex_to_byte(frame[12:])
    }

class Pylontech:
    def __init__(self,
        baudrate=115200,
        pins=None,
        uart_id=0,
        timeout=1000
      ):
        self.s = UART(
          uart_id,
          baudrate=baudrate,
          tx=pins[0],
          rx=pins[1],
          timeout=timeout
        )

    def send_cmd(self, address, cmd, info = b''):
        raw_frame = _encode_cmd(address, cmd, info)
        self.s.write(raw_frame)

    def read_frame(self):
        raw_frame = self.s.readline()

        f = _decode_hw_frame(raw_frame=raw_frame)
        parsed = _decode_frame(f)

        return parsed

    def get_values(self, dev_id):
        b_dev_id = "{:02X}".format(dev_id).encode()
        self.send_cmd(dev_id, 0x42, b_dev_id)
        f = self.read_frame()

        info = f['info'][1:]

        def next(count=1):
            nonlocal info

            val = info[0:count]
            info = info[count:]

            return val

        NumberOfModule = int.from_bytes(next(), 'big', False)
        NumberOfCells = int.from_bytes(next(), 'big', False)
        CellVoltages = [int.from_bytes(next(2), 'big', False) / 1000 for x in range(0, NumberOfCells)]
        NumberOfTemperatures = int.from_bytes(next(), 'big', False)
        AverageBMSTemperature = (int.from_bytes(next(2), 'big', True) - 2731) / 10
        GroupedCellsTemperatures = [(int.from_bytes(next(2), 'big', True) - 2731) / 10 for x in range(1, NumberOfTemperatures)]
        Current = int.from_bytes(next(2), 'big', True) / 1000
        Voltage = int.from_bytes(next(2), 'big', False) / 1000
        Power = Current * Voltage
        RemainingCapacity1 = int.from_bytes(next(2), 'big', False) / 1000
        UserDefinedItems = int.from_bytes(next(), 'big', False)
        Capacity1 = int.from_bytes(next(2), 'big', False) / 1000
        CycleNumber = int.from_bytes(next(2), 'big', False)
        OptionalFields = {
          'RemainingCapacity2': int.from_bytes(next(3), 'big', False) / 1000,
          'Capacity2': int.from_bytes(next(3), 'big', False) / 1000
        } if UserDefinedItems > 2 else None
        RemainingCapacity = OptionalFields['RemainingCapacity2'] if UserDefinedItems > 2 else RemainingCapacity1
        Capacity = OptionalFields['Capacity2'] if UserDefinedItems > 2 else Capacity1
        StateOfCharge = RemainingCapacity / Capacity

        return {
          'NumberOfModule': NumberOfModule,
          'NumberOfCells': NumberOfCells,
          'CellVoltages': CellVoltages,
          'NumberOfTemperatures': NumberOfTemperatures,
          'AverageBMSTemperature': AverageBMSTemperature,
          'GroupedCellsTemperatures': GroupedCellsTemperatures,
          'Current': Current,
          'Voltage': Voltage,
          'Power': Power,
          'CycleNumber': CycleNumber,
          'RemainingCapacity': RemainingCapacity,
          'Capacity': Capacity,
          'StateOfCharge': StateOfCharge
        }

if __name__ == '__main__':
    p = Pylontech(uart_id=1, pins=[Pin(4), Pin(5)])

    result = {}

    for x in range(2, 5):
        v = None
        try:
            v = p.get_values(x)
        except AssertionError:
            print("Cannot access device")
        finally:
            result[x] = v

    print(result)

