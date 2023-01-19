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
            'WorkState': ['PowerOn', 'SelfTest', 'OffGrid', 'Grid-Tie', 'ByPass', 'Stop'][info[0]],
            'BatteryVoltage': info[4] / 10,
            'InverterVoltage': info[5] / 10,
            'GridVoltage': info[6] / 10,
            'InverterCurrent': info[9] / 10,
            'GridCurrent': info[10] / 10,
            'InverterPower': info[12],
            'GridPower': info[13],
            'LoadPower': info[14],
            'Load': info[15] / 100,
            'InverterFrequency': info[24] / 100,
            'GridFrequency': info[25] / 100,
            'ACRadiatorTemperature': info[32],
            'TransformerTemperature': info[33],
            'DCRadiatorTemperature': info[34],
            'BatteryPower': info[72],
            'BatteryCurrent': info[73],
        }


if __name__ == '__main__':
    m = Must(uart_id=0, pins=[Pin(0), Pin(1)], ctrl_pin=5)
    print(m.get_values())


