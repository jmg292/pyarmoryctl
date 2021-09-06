import re
from pathlib import Path

class AnnaB112Configuration(object):

    def __init__(self):

        # Serial communication configuration
        self.uart_device = "/dev/ttymxc0"
        self.uart_speed = "115200"
        self.message_received_expression = re.compile('"[^"]+"|OK')

        # Constants
        self.bootloader_offset = 0x78000
        self.soft_device_crc_offset = 0x7e000
        self.flash_size = 524_288
        self.customer_31_nrf_52_uicr_offset = 0x0fc

        # Templates
        self.template_path = Path().absolute().joinpath("app_config", "anna_b112", "templates")

        # Tags
        self.bootloader_tag = "Bootloader"
        self.connectivity_software_tag = "ConnectivitySoftware"
        self.soft_device_tag = "SoftDevice"

        
