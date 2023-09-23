from time import time

import pytest

from domain.exceptions import BusinessRuleValidationException
from domain.microwave_oven import MicrowaveOven


def test_oven_is_turn_on_when_power_is_greater_than_0():
    oven = MicrowaveOven(time(), 10)
    assert oven.state == "ON"


def test_oven_is_turn_on_when_time_is_greater_than_0():
    future = time() + 1
    oven = MicrowaveOven(future, 0)
    assert oven.state == "ON"


def test_oven_to_dict():
    future = time() + 5
    oven = MicrowaveOven(future, 10)
    assert {"state": "ON", "power": 10, "counter": 5} == oven.to_dict()


def test_oven_is_turn_off_after_canceling():
    future = time() + 10
    oven = MicrowaveOven(future, 0)
    oven.cancel()
    assert oven.state == "OFF"


def test_set_time_first_time_on_oven_should_turn_on_oven():
    oven = MicrowaveOven(time(), 0)
    oven.increase_time(10)
    assert oven.state == "ON"


def test_set_power_first_time_on_oven_should_turn_on_oven():
    oven = MicrowaveOven(time(), 0)
    oven.increase_power(10)
    assert oven.state == "ON"


def test_oven_is_turn_of_when_time_is_not_passed_yet():
    future = time() + 10
    oven = MicrowaveOven(future, 0)
    assert oven.state == "ON"


def test_oven_is_turn_of_when_time_passed():
    past = time() - 10
    oven = MicrowaveOven(past, 0)
    assert oven.state == "OFF"


def test_could_not_decrease_time_to_less_than_0():
    future = time() + 10
    oven = MicrowaveOven(future, 0)
    with pytest.raises(BusinessRuleValidationException):
        oven.decrease_time(12)


def test_oven_is_still_on_when_decreased_time_is_still_in_the_future():
    future = time() + 10
    oven = MicrowaveOven(future, 0)
    oven.decrease_time(1)
    assert oven.state == "ON"


def test_oven_is_switched_to_off_when_someone_turn_power_off():
    oven = MicrowaveOven(time(), 10)
    oven.decrease_power(10)
    assert oven.state == "OFF"
