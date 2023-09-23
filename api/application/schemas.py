from pydantic import BaseModel


class Microwave(BaseModel):
    counter: int
    power: int
    state: power
