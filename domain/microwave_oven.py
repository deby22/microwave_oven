from typing import Type

from domain.exceptions import BusinessRuleValidationException
from domain.power import Power
from domain.seconds import Seconds
from domain.time_provider import RealTimeProvider, TimeProvider


class MicrowaveOven:
    def __init__(
        self,
        init_counter: int,
        init_power: int,
        time_provider_cls: Type[TimeProvider] = RealTimeProvider,
    ):
        self._counter = Seconds(init_counter)
        self._power = Power(init_power)
        self._time_provider = time_provider_cls()
        self._set_initial_last_turning_on()

    def to_dict(self):
        return {"state": self.state, "power": self._power, "counter": self._counter}

    @property
    def state(self) -> str:
        return "OFF" if self._time_expired() and not self._power else "ON"

    def cancel(self):
        self._counter = Seconds(0)
        self._power = Power(0)

    def _set_initial_last_turning_on(self):
        if self._counter:
            self.last_turning_on = self._time_provider.get_current_time()
        else:
            self.last_turning_on = None

    def _time_expired(self):
        if not self._counter:
            return True
        if not self.last_turning_on:
            return True
        current_time = self._time_provider.get_current_time()
        asd = bool(self._counter + self.last_turning_on < current_time)
        return asd

    def _set_last_turning_on_if_needed(self):
        if self._time_expired():
            self.last_turning_on = self._time_provider.get_current_time()

    def increase_time(self, value):
        self._counter += value
        self._set_last_turning_on_if_needed()

    def decrease_time(self, value):
        if self._counter - value < 1:
            raise BusinessRuleValidationException(
                "You cannot set timer to 0. Use cancled button instead"
            )
        self._counter -= value

    def increase_power(self, value):
        self._power += value

    def decrease_power(self, value):
        self._power -= value
