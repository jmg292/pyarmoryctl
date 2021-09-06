import logging
import serial

from ..app_config.configuration import ApplicationConfiguration


class AnnaB112DeviceInterface(object):

    def __init__(self, *args, **kwargs):
        self._log = logging.getLogger()
        self._uart_connection: serial.Serial = None
        self._configuration: ApplicationConfiguration = kwargs.get("configuration")
        if not self._configuration:
            raise ValueError("Configuration value must be supplied.")

    def _send_command(self, command: str):
        if not command:
            raise ValueError("Command must not be empty.")
        if not self._uart_connection:
            raise ConnectionError("Not connected to bluetooth module")

    def connect(self, device_path: str = "", baud_rate: int = -1):
        self._log.debug(f"Connecting to bluetooth serial interface at {device_path}")
        self._uart_connection = serial.Serial(port=device_path, baudrate=baud_rate)
