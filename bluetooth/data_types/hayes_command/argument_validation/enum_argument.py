from enum import Enum


class EnumTypeValidator(object):

    def __init__(self, enum_type: Enum):
        self.enum_type = enum_type
        self.value = None