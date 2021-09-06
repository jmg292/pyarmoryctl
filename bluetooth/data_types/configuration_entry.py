class ConfigurationEntry(object):

    def __init__(self, *args, **kwargs):
        self.label: str = ""
        self.description: str = ""
        self.file: str = ""
        self.version: str = ""
        self.address: str = ""
        self.size: str = ""
        self.checksum_crc32: str = ""
