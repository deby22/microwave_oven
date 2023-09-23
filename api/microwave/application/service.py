from pydantic import NegativeInt, PositiveInt

from microwave.application.schemas import Microwave as MicrowaveDTO
from microwave.domain.microwave_oven import MicrowaveOven as MicrowaveEntity
from microwave.domain.repository import IMicrowaveRepository
from microwave.infrastructure.repositories.in_memory import InMemoryRepository

IN_MEMORY_REPO = InMemoryRepository()


class ApplicationService:
    def __init__(self, repo: IMicrowaveRepository = IN_MEMORY_REPO):
        self._repo = repo

    def get_state(self):
        data = self._repo.read()
        microwave = MicrowaveEntity(**data)
        return MicrowaveDTO(**microwave.to_dict())

    def update_power(self, value: NegativeInt | PositiveInt) -> MicrowaveDTO:
        data = self._repo.read()
        microwave = MicrowaveEntity(**data)
        if value > 0:
            microwave.increase_power(value)
        elif value < 0:
            microwave.decrease_power(abs(value))
        self._repo.save(microwave.to_dict())
        return MicrowaveDTO(**microwave.to_dict())

    def update_counter(self, value: NegativeInt | PositiveInt) -> MicrowaveDTO:
        data = self._repo.read()
        microwave = MicrowaveEntity(**data)
        if value > 0:
            microwave.increase_time(value)
        elif value < 0:
            microwave.decrease_time(abs(value))
        self._repo.save(microwave.to_dict())
        return MicrowaveDTO(**microwave.to_dict())

    def cancel(self) -> MicrowaveDTO:
        data = self._repo.read()
        microwave = MicrowaveEntity(**data)
        microwave.cancel()
        self._repo.save(microwave.to_dict())
        return MicrowaveDTO(**microwave.to_dict())
