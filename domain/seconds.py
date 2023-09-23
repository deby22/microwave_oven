from dataclasses import dataclass

from domain.exceptions import BusinessRuleValidationException
from domain.value_object import ValueObject


@dataclass(frozen=True)
class Seconds(ValueObject):
    value: int

    def __post_init__(self):
        if self.value < 0:
            raise BusinessRuleValidationException("Seconds should be greater than 0")

    def __add__(self, value: int | float) -> "Seconds":
        return Seconds(value=(value + self.value))

    def __sub__(self, value: int | float) -> "Seconds":
        return Seconds(value=(self.value - value))

    def __bool__(self) -> bool:
        return self.value != 0

    def __lt__(self, other: int | float) -> bool:
        return self.value < other

    def __int__(self):
        return self.value
