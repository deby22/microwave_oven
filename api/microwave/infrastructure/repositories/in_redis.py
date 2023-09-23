import json

from microwave.domain.repository import IMicrowaveRepository
from microwave.infrastructure.dto import Microwave as MicrowaveDTO


class RedisRepository(IMicrowaveRepository):
    def __init__(self, connector):
        self._connector = connector

    def read(self):
        data = self._connector.get("microwave")
        try:
            parsed_data = json.loads(data)
        except TypeError:
            return MicrowaveDTO(power=0).dict()
        return MicrowaveDTO(**parsed_data).dict()

    def save(self, data: dict):
        microwave = MicrowaveDTO(**data)
        parsed_data = microwave.dict(exclude_defaults=True)
        self._connector.set("microwave", json.dumps(parsed_data))
