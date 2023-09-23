from typing import Optional

from pydantic import BaseModel, NonNegativeInt

from microwave.domain.repository import IMicrowaveRepository


class Microwave(BaseModel):
    turn_of_time: Optional[float]
    power: NonNegativeInt


class InMemoryRepository(IMicrowaveRepository):
    def __init__(self):
        self._data = Microwave(turn_of_time=None, power=0)

    def read(self):
        return self._data.dict()

    def save(self, data: dict):
        self._data = Microwave(**data)
