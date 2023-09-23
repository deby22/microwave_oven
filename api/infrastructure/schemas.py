from typing import Optional

from redis_om import HashModel

from config import redis_db


class Microwave(HashModel):
    power: int
    turn_of_time: Optional[float]

    class Meta:
        database: redis_db
