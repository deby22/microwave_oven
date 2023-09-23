from typing import Optional

from pydantic import BaseModel, Field, NonNegativeInt


class Microwave(BaseModel):
    turn_of_time: Optional[float] = Field(default=None)
    power: NonNegativeInt
