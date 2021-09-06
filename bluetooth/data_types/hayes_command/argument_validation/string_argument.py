class StringValidator(object):

    def __init__(self, max_length=-1):
        self.max_length = max_length
        self.value = None