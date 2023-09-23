from time import time
from typing import Optional

from domain.exceptions import BusinessRuleValidationException
from domain.power import Power
from domain.seconds import Seconds


class MicrowaveOven:
    def __init__(
        self,
        turn_of_time: Optional[float] = None,
        power: Optional[float] = None,
    ):
        self._turn_of_time = turn_of_time
        self._power = Power(power or 0)

    def _counter(self):
        if not self._turn_of_time:
            return Seconds(0)
        if self._time_expired():
            return Seconds(0)
        return Seconds(round(self._turn_of_time - time()))

    def to_dict(self):
        return {
            "state": self.state,
            "power": int(self._power),
            "counter": int(self._counter()),
        }

    @property
    def state(self) -> str:
        return "OFF" if self._time_expired() and not self._power else "ON"

    def cancel(self):
        self._turn_of_time = time()
        self._power = Power(0)

    def _time_expired(self):
        if not self._turn_of_time:
            return True
        return self._turn_of_time <= time()

    def increase_time(self, value):
        if self._time_expired():
            self._turn_of_time = time() + value
        self._turn_of_time += value

    def decrease_time(self, value):
        if not self._turn_of_time:
            raise BusinessRuleValidationException(
                "Cannot decrease time. Microwave is turn off"
            )
        if self._turn_of_time - value < time():
            raise BusinessRuleValidationException("Seconds should be greater than 0")
        self._turn_of_time -= value

    def increase_power(self, value):
        self._power += value

    def decrease_power(self, value):
        self._power -= value
