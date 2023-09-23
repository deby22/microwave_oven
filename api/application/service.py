from typing import Type

from application.schemas import Microwave as MicrowaveDTO
from domain.microwave_oven import MicrowaveOven as MicrowaveEntity
from domain.repository import IMicrowaveRepository
from infrastructure.repositories.in_memory import InMemoryRepository


class ApplicationService:
    def __init__(self, repo: Type[IMicrowaveRepository] = InMemoryRepository):
        self._repo = repo()

    def get_state(self):
        data = self._repo.read()
        microwave = MicrowaveEntity(**data)
        return MicrowaveDTO(**microwave.to_dict())
