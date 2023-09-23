from domain.repository import IMicrowaveRepository


class InMemoryRepository(IMicrowaveRepository):
    def __init__(self):
        self._data = {"turn_of_time": None, "power": 0}

    def read(self):
        return self._data

    def save(self, data: dict):
        self._data = data
