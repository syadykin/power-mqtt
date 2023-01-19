# state registers
# device id 4
# baudrate 19200
# holding register start 25201, qty 74

data = [
  2,      # WorkState 0:PowerOn 1:SelfTest 2:OffGrid 3:Grid-Tie 4:ByPass 5:Stop
  230,    # ACVoltageGrade 230/120, V
  5000,   # RatedPower, W
  0,      # reserved
  497,    # BatteryVoltage, 0.1V
  2299,   # InverterVoltage, 0.1V
  0,      # GridVoltage, 0.1V
  3962,   # BusVoltage, 0.1V (?)
  43,     # ControlCurrent, 0.1A
  43,     # InverterCurrent, 0.1A
  0,      # GridCurrent, 0.1A
  33,     # LoadCurrent, 0.1A
  562,    # PowerInverter, 1W
  0,      # PowerGrid, 1W
  555,    # PowerLoad, 1W
  11,     # LoadPercent, %
  1008,   # SInverter, 1VA (?)
  0,      # SGrid, 1VA (?)
  753,    # SLoad, 1VA (?)
  0,      # reserved
  821,    # QInverter, 1var (?)
  0,      # QGrid, 1var (?)
  508,    # QLoad, 1var (?)
  0,      # reserved
  5000,   # InverterFrequency, 0.01Hz
  0,      # GridFrequency, 0.01Hz
  0,      # reserved
  0,      # reserved
  0,      # InverterMaxNumber (?)
  0,      # CombineType (?)
  0,      # InverterNumber (?)
  0,      # reserved
  35,     # ACRadiatorTemperature, 1°C
  49,     # TransformerTemperature, 1°C
  28,     # DCRadiatorTemperature, 1°C
  0,      # reserved
  1,      # InverterRelayState, 0: Disconnect 1:Connect
  0,      # GridRelayState, 0: Disconnect 1:Connect
  1,      # LoadRelayState, 0: Disconnect 1:Connect
  0,      # N_LineRelayState, 0: Disconnect 1:Connect
  1,      # DCRelayState, 0: Disconnect 1:Connect
  0,      # EarthRelayState, 0: Disconnect 1:Connect
  0,      # reserved
  0,      # reserved
  0,      # Accumulated, PH?
  888,    # Accumulated, PH?
  0,      # Accumulated, PH?
  611,    # Accumulated, PH?
  0,      # Accumulated, PH?
  2443,   # Accumulated, PH?
  0,      # Accumulated, PH?
  0,      # Accumulated, PH?
  0,      # Accumulated, PH?
  2114,   # Accumulated, PH?
  0,      # Accumulated, PH?
  33,     # Accumulated, PH?
  0,      # Accumulated, PH?
  0,      # Accumulated, PH?
  0,      # Accumulated, PH?
  888,    # Accumulated, PH?
  0,      # ErrorMessage1
  0,      # ErrorMessage2
  0,      # ErrorMessage3
  0,      # reserved
  0,      # WarningMessage1
  0,      # WarningMessage2
  0,      # reserved
  0,      # reserved
  -1,     # SerialNumberHigh
  -1,     # SerialNumberLow
  10101,  # HardwareVersion
  21706,  # SoftwareVersion
  659,    # BatteryPower, 1W
  13      # BatteryCurrent, 1A
]

values = {
  'InverterVoltage': 229.7,
  'BatteryCurrent': 17,
  'InverterPower': 761,
  'BatteryVoltage': 50.47059,
  'GridVoltage': 0.0,
  'GridPower': 0,
  'InverterFrequency': 5000,
  'GridCurrent': 0.0,
  'ACRadiatorTemperature': 36,
  'TransformerTemperature': 50,
  'InverterCurrent': 5.1,
  'DCRadiatorTemperature': 27,
  'WorkState': 'OffGrid',
  'Load': 0.14,
  'GridFrequency': 0,
  'LoadPower': 709,
  'BatteryPower': 858
}

class Must:
    def __init__(self,
        baudrate=19200,
        pins=None,
        ctrl_pin=None,
        uart_id=0):

        pass

    def get_values(addr=4):
        return values
