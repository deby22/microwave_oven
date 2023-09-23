from domain.repository import IMicrowaveRepository
from infrastructure.schemas import Microwave


class RedisRepository(IMicrowaveRepository):
    def read(self):
        return Microwave.get("microwave")

    def save(self, data: dict):
        Microwave(**data).save()
