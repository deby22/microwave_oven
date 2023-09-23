from enum import Enum

from pydantic import BaseModel


class StateEnum(str, Enum):
    on = "ON"
    off = "OFF"


class Microwave(BaseModel):
    counter: int
    power: int
    state: StateEnum
