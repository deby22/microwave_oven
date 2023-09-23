from redis_om import HashModel

from config import redis_db


class Microwave(HashModel):
    counter: int
    power: int
    last_turning_on: float

    class Meta:
        database: redis_db
