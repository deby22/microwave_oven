from dataclasses import dataclass

from api.domain.exceptions import BusinessRuleValidationException
from api.domain.value_object import ValueObject


@dataclass(frozen=True)
class Power(ValueObject):
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise BusinessRuleValidationException("Power should be greater than 0")

        if self.value > 100:
            raise BusinessRuleValidationException("Power should be lower than 100")

    def __add__(self, value: int) -> "Power":
        return Power(value=(value + self.value))

    def __sub__(self, value: int) -> "Power":
        return Power(value=(value - self.value))

    def __bool__(self) -> bool:
        return self.value != 0

    def __int__(self):
        return self.value
