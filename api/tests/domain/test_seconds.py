import pytest

from api.domain.exceptions import BusinessRuleValidationException
from api.domain.seconds import Seconds


def test_time_could_not_be_lower_than_0():
    with pytest.raises(BusinessRuleValidationException):
        Seconds(-1)


def test_power_should_be_created_with_valid_value():
    assert Seconds(0).value == 0
    assert Seconds(100).value == 100
    assert Seconds(1000).value == 1000


def test_decrease_time():
    assert Seconds(0) == Seconds(10) - 10
    assert Seconds(1) == Seconds(10) - 9


def test_increase_time():
    assert Seconds(20) == Seconds(10) + 10


def test_boolean_comparision():
    assert bool(Seconds(0)) is False
    assert bool(Seconds(1)) is True
