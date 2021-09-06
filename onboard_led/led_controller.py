from onboard_led.led_state import LEDState
import gpio
from .led_color import LEDColor
from .led_state import LEDState


class OnboardLEDController(object):

    def __init__(self, led_color: LEDColor):
        self._current_state = None
        self._onboard_led = led_color
        self._set_led_state(LEDState.Off)

    def _set_led_state(self, new_state: LEDState):
        if self._current_state == new_state:
            return
        gpio.output(self._onboard_led, new_state)
        self._current_state = new_state
