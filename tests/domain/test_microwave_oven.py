from time import time

import pytest

from domain.exceptions import BusinessRuleValidationException
from domain.microwave_oven import MicrowaveOven
from domain.time_provider import TimeProvider


class DummyTimeProvider(TimeProvider):
    def get_current_time(self):
        return self.times.pop()


class InThePastTimeProvider(DummyTimeProvider):
    def __init__(self):
        self.times = [time() - 1, time() - 10]


class InTheFutureTimeProvider(DummyTimeProvider):
    def __init__(self):
        self.times = [time() + 10, time() - 10]


def test_oven_is_turn_on_when_power_is_greater_than_0():
    oven = MicrowaveOven(0, 10)
    assert oven.state == "ON"


def test_oven_is_turn_on_when_time_is_greater_than_0():
    oven = MicrowaveOven(10, 0)
    assert oven.state == "ON"


def test_oven_is_turn_off_after_canceling():
    oven = MicrowaveOven(10, 0)
    oven.cancel()
    assert oven.state == "OFF"


def test_set_time_first_time_on_oven_should_turn_on_oven():
    oven = MicrowaveOven(0, 0)
    oven.increase_time(10)
    assert oven.state == "ON"


def test_set_power_first_time_on_oven_should_turn_on_oven():
    oven = MicrowaveOven(0, 0)
    oven.increase_power(10)
    assert oven.state == "ON"


def test_oven_is_turn_of_when_time_is_not_passed_yet():
    oven = MicrowaveOven(10, 0, InThePastTimeProvider)
    assert oven.state == "ON"


def test_oven_is_turn_of_when_time_is_passed():
    oven = MicrowaveOven(10, 0, InTheFutureTimeProvider)
    assert oven.state == "OFF"


def test_could_not_decrease_time_to_less_than_1():
    oven = MicrowaveOven(10, 0)
    with pytest.raises(BusinessRuleValidationException):
        oven.decrease_time(10)


def test_oven_is_still_on_when_decreased_time_is_still_in_the_future():
    oven = MicrowaveOven(10, 0, InThePastTimeProvider)
    oven.decrease_time(1)
    assert oven.state == "ON"


def test_oven_is_switched_to_off_when_someone_turn_power_off():
    oven = MicrowaveOven(0, 10)
    oven.decrease_power(10)
    assert oven.state == "OFF"
