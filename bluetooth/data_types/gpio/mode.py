from enum import IntEnum

class GpioMode(IntEnum):

    Output = 0x00
    Input = 0x01
    Disabled = 0xFF
