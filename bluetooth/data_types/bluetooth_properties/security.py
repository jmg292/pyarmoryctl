from enum import IntEnum


class SecurityMode(IntEnum):

    Disabled = 1
    JustWorks = 2
    DisplayOnly = 3
    DisplayPrompt = 4
    KeyboardOnly = 5
    OutOfBand = 6


class SecurityModeSetting(IntEnum):

    Disabled = 0
    Bluetooth2FixedPin = 1
    BluetoothLEHeadlessFixedPin = 2
    MultiModeHeadlessFixedPin = 3


class SecurityType(IntEnum):

    SecureSimplePairing = 0
    EC_P_256_AES_CCM = 1
    FIPS = 2
