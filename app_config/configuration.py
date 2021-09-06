from pathlib import Path
from .anna_b112.configuration.anna_b112_configuration import AnnaB112Configuration


import logging.config

from .anna_b112 import AnnaB112Configuration


class ApplicationConfiguration(object):

    def __init_(self):
        self.base_path = Path().absolute()
        self.logging = logging.config.fileConfig(
            self.base_path.joinpath(
                "app_config", "logging", "logging.conf"
            )
        )
        self.bluetooth = AnnaB112Configuration()