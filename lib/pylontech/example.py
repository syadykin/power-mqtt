# rs485 response example for 3 battery packs
# baudrate=115200

data = [
    b'\x11\x02\x0f\x0c\xee\x0c\xef\x0c\xef\x0c\xef\x0c\xef\x0c\xee\x0c\xef\x0c\xef\x0c\xf0\x0c\xef\x0c\xee\x0c\xef\x0c\xef\x0c\xef\x0c\xef\x05\x0b\xcc\x0b\xbe\x0b\xbe\x0b\xb9\x0b\xbf\xff\xdb\xc1\xff\xff\xff\x04\xff\xff\x00\x06\x00\xf5\xb4\x01!\x10',
    b'\x11\x03\x0f\x0c\xec\x0c\xed\x0c\xed\x0c\xed\x0c\xed\x0c\xec\x0c\xed\x0c\xed\x0c\xed\x0c\xed\x0c\xec\x0c\xed\x0c\xec\x0c\xed\x0c\xed\x05\x0b\xc3\x0b\xba\x0b\xba\x0b\xb9\x0b\xb6\xff\xdc\xc1\xdf\xff\xff\x04\xff\xff\x00\x05\x00\xf5\xb4\x01!\x10',
    b'\x11\x04\x0f\x0c\xec\x0c\xec\x0c\xec\x0c\xec\x0c\xec\x0c\xeb\x0c\xeb\x0c\xec\x0c\xec\x0c\xed\x0c\xec\x0c\xec\x0c\xec\x0c\xed\x0c\xed\x05\x0b\xbc\x0b\xb2\x0b\xb1\x0b\xb1\x0b\xb5\xff\xdb\xc1\xd5\xff\xff\x04\xff\xff\x00\x05\x00\xf5\xb4\x01!\x10'
]

values = {
  '2': {
    'RemainingCapacity': 60.68,
    'Capacity': 74.0,
    'StateOfCharge': 0.82,
    'NumberOfCells': 15,
    'NumberOfModule': 2,
    'NumberOfTemperatures': 5,
    'GroupedCellsTemperatures': [27.5, 27.4, 27.0, 27.7],
    'Current': 65.482,
    'CycleNumber': 6,
    'CellVoltages': [3.304, 3.304, 3.304, 3.303, 3.304, 3.303, 3.303, 3.304, 3.305, 3.304, 3.303, 3.303, 3.303, 3.304, 3.304],
    'AverageBMSTemperature': 29.1,
    'Power': 3244.961,
    'Voltage': 49.555
  },
  '3': {
    'RemainingCapacity': 60.68,
    'Capacity': 74.0,
    'StateOfCharge': 0.82,
    'NumberOfCells': 15,
    'NumberOfModule': 3,
    'NumberOfTemperatures': 5,
    'GroupedCellsTemperatures': [27.1, 27.1, 26.9, 27.0],
    'Current': 65.482,
    'CycleNumber': 6,
    'CellVoltages': [3.304, 3.304, 3.303, 3.304, 3.303, 3.303, 3.304, 3.304, 3.303, 3.303, 3.304, 3.304, 3.303, 3.304, 3.303],
    'AverageBMSTemperature': 28.1,
    'Power': 3244.830,
    'Voltage': 49.553
  },
  '4': {
    'RemainingCapacity': 60.68,
    'Capacity': 74.0,
    'StateOfCharge': 0.82,
    'NumberOfCells': 15,
    'NumberOfModule': 4,
    'NumberOfTemperatures': 5,
    'GroupedCellsTemperatures': [26.3, 26.1, 26.1, 26.8],
    'Current': 65.484,
    'CycleNumber': 6,
    'CellVoltages': [3.304, 3.304, 3.304, 3.304, 3.303, 3.303, 3.303, 3.303, 3.303, 3.304, 3.304, 3.304, 3.304, 3.304, 3.304],
    'AverageBMSTemperature': 27.4,
    'Power': 3245.060,
    'Voltage': 49.555
  }
}


class Pylontech:
    def __init__(self,
        baudrate=115200,
        pins=None,
        uart_id=0,
        timeout=1000
      ):
      pass

    def get_values(self, battery=2):
        return values[str(battery)]

