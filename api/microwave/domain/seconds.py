from dataclasses import dataclass

from microwave.domain.exceptions import BusinessRuleValidationException
from microwave.domain.value_object import ValueObject


@dataclass(frozen=True)
class Seconds(ValueObject):
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise BusinessRuleValidationException("Seconds should be greater than 0")

    def __add__(self, value: int | float) -> "Seconds":
        return Seconds(value=round(value + self.value))

    def __sub__(self, value: float | int) -> "Seconds":
        return Seconds(value=round(self.value - value))

    def __bool__(self) -> bool:
        return self.value != 0

    def __int__(self):
        return round(self.value)
