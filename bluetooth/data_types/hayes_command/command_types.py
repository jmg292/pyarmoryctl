class BasicCommand(object):

    PREFIX = "+"
    COMMAND = "Undefined"

    def __init__(self, *args):
        self.command_arguments = list(args)


class ReadWriteCommand(BasicCommand):
    pass


class ExtendedCommand(BasicCommand):

    PREFIX = "&"
    

class ProprietaryCommand(BasicCommand):

    PREFIX = "%"


class RegisterCommand(BasicCommand):

    def __init__(self):
        self._command_arguments = []
        self.execute_as_query = False
