import pytest

from microwave.domain.power import BusinessRuleValidationException, Power


def test_power_could_not_be_lower_than_0():
    with pytest.raises(BusinessRuleValidationException):
        Power(-1)


def test_power_could_not_be_greater_than_100():
    with pytest.raises(BusinessRuleValidationException):
        Power(101)


def test_power_should_be_created_with_valid_value():
    assert Power(0).value == 0
    assert Power(100).value == 100
    assert Power(50).value == 50


def test_decrease_power():
    assert Power(0) == Power(10) - 10
    assert Power(1) == Power(10) - 9


def test_increase_power():
    assert Power(20) == Power(10) + 10


def test_boolean_comparision():
    assert bool(Power(0)) is False
    assert bool(Power(1)) is True
