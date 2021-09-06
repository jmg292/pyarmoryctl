from enum import IntFlag, auto


class OperationalMode(IntFlag):

    Classic = auto()
    LowEnergy = auto()
    Mesh = auto()

