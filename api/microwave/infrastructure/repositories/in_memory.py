from microwave.domain.repository import IMicrowaveRepository
from microwave.infrastructure.dto import Microwave as MicrowaveDTO


class InMemoryRepository(IMicrowaveRepository):
    def __init__(self):
        self._data = MicrowaveDTO(turn_of_time=None, power=0)

    def read(self):
        return self._data.dict()

    def save(self, data: dict):
        self._data = MicrowaveDTO(**data)
