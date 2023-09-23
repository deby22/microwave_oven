from dataclasses import dataclass

from domain.exceptions import BusinessRuleValidationException


@dataclass(frozen=True)
class Seconds:
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