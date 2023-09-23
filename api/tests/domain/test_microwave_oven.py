from time import time

import pytest

from microwave.domain.exceptions import BusinessRuleValidationException
from microwave.domain.microwave_oven import MicrowaveOven


class TestPower:
    def test_set_power_first_time_on_oven_should_turn_on_oven(self):
        oven = MicrowaveOven(time(), 0)
        oven.increase_power(10)
        assert oven.state == "ON"

    def test_oven_is_switched_to_off_when_someone_turn_power_off(self):
        oven = MicrowaveOven(time(), 10)
        oven.decrease_power(10)
        assert oven.state == "OFF"


class TestCounter:
    def test_decrease_time_is_allowed_only_on_previously_working_oven(self):
        oven = MicrowaveOven(None, 0)
        with pytest.raises(BusinessRuleValidationException):
            oven.decrease_time(12)

    def test_set_time_first_time_on_oven_should_turn_on_oven(self):
        oven = MicrowaveOven(time(), 0)
        oven.increase_time(10)
        assert oven.state == "ON"

    def test_could_not_decrease_time_to_less_than_0(self):
        future = time() + 10
        oven = MicrowaveOven(future, 0)
        with pytest.raises(BusinessRuleValidationException):
            oven.decrease_time(12)

    def test_oven_is_still_on_when_decreased_time_is_still_in_the_future(self):
        future = time() + 10
        oven = MicrowaveOven(future, 0)
        oven.decrease_time(1)
        assert oven.state == "ON"


class TestCancel:
    def test_oven_is_turn_off_after_canceling(self):
        future = time() + 10
        oven = MicrowaveOven(future, 0)
        oven.cancel()
        assert oven.state == "OFF"


class TestDefaultState:
    def test_oven_is_turn_on_when_power_is_greater_than_0(self):
        oven = MicrowaveOven(time(), 10)
        assert oven.state == "ON"

    def test_oven_is_turn_on_when_time_is_greater_than_0(self):
        future = time() + 1
        oven = MicrowaveOven(future, 0)
        assert oven.state == "ON"

    def test_oven_is_turn_of_when_time_passed_and_power_is_equals_to_zero(self):
        past = time() - 10
        oven = MicrowaveOven(past, 0)
        assert oven.state == "OFF"

    def test_oven_is_turn_on_when_time_passed_and_power_is_greater_than_0(self):
        past = time() - 10
        oven = MicrowaveOven(past, 1)
        assert oven.state == "ON"

    def test_state_should_be_off_when_oven_was_never_turned_on_and_has_no_power(self):
        oven = MicrowaveOven(None, 0)
        assert oven.state == "OFF"

    def test_state_should_be_on_when_oven_was_never_turned_on_but_has_power_set(self):
        oven = MicrowaveOven(None, 10)
        assert oven.state == "ON"


class TestDictRepresentation:
    def test_oven_to_dict_when_is_on(self):
        future = time() + 5
        oven = MicrowaveOven(future, 10)
        assert {
            "state": "ON",
            "power": 10,
            "counter": 5,
            "turn_of_time": future,
        } == oven.to_dict()

    def test_oven_to_dict_when_was_never_turned_on(self):
        oven = MicrowaveOven(None, 10)
        assert {
            "state": "ON",
            "power": 10,
            "counter": 0,
            "turn_of_time": None,
        } == oven.to_dict()

    def test_oven_should_be_still_on_but_counter_shows_0_when_time_is_from_past(self):
        """Microwave is ON when Power or Counter are greater than zero"""
        past = time() - 1
        oven = MicrowaveOven(past, 10)
        assert {
            "state": "ON",
            "power": 10,
            "counter": 0,
            "turn_of_time": past,
        } == oven.to_dict()
