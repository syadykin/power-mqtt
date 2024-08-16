from machine import Pin
from umodbus.serial import Serial as ModbusRTU

class Must:
    def __init__(self,
        baudrate=19200,
        pins=None,
        ctrl_pin=None,
        uart_id=0):

        self.m = ModbusRTU(
            uart_id=uart_id,
            baudrate=baudrate,
            pins=pins,
            ctrl_pin=ctrl_pin)

    def get_values(self, addr=4):
        info = self.m.read_holding_registers(
            slave_addr=addr,
            starting_addr=25201,
            register_qty=74)

        return {
            # 25201
            'WorkState': ['PowerOn', 'SelfTest', 'OffGrid', 'Grid-Tie', 'ByPass', 'Stop'][info[0]],
            # 25205
            'BatteryVoltage': info[4] / 10,
            # 25206
            'InverterVoltage': info[5] / 10,
            # 25207
            'GridVoltage': info[6] / 10,
            # 25210
            'InverterCurrent': info[9] / 10,
            # 25211
            'GridCurrent': info[10] / 10,
            # 25213
            'InverterPower': info[12],
            # 25214
            'GridPower': info[13],
            # 25215
            'LoadPower': info[14],
            # 25216
            'Load': info[15] / 100,
            # 25225
            'InverterFrequency': info[24] / 100,
            # 25226
            'GridFrequency': info[25] / 100,
            # 25233
            'ACRadiatorTemperature': info[32],
            # 25234
            'TransformerTemperature': info[33],
            # 25235
            'DCRadiatorTemperature': info[34],
            # 25273
            'BatteryPower': info[72],
            # 25274
            'BatteryCurrent': info[73],
        }


if __name__ == '__main__':
    m = Must(uart_id=0, pins=[Pin(0), Pin(1)], ctrl_pin=5)
    print(m.get_values())


