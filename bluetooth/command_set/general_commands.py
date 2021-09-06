from ..data_types.system_properties import GreetingTextMode
from ..data_types.hayes_command.argument_validation import StringValidator, EnumTypeValidator
from ..data_types.hayes_command.command_types import BasicCommand, RegisterCommand


class GetManufacturerIdentification(BasicCommand): 
    
    COMMAND = "CGMI"


class GetModelIdentification(BasicCommand): 

    COMMAND = "CGMM"


class GetSoftwareVersion(BasicCommand): 
    
    COMMAND = "CGMR"


class GetSerialNumber(BasicCommand): 
    
    COMMAND = "CGSN"


class GreetingText(RegisterCommand):

    COMMAND = "CSGT"
    DisplayMode: GreetingTextMode = None
    


    @property
    def display_mode(self, value: GreetingTextMode):
        if type(value) is not 