from enum import IntEnum


class GpioInputResistor(IntEnum):

    NoResistor = 0
    PullUpResistor = 1
    PullDownResistor = 2
