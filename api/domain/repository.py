from abc import ABC


class IMicrowaveRepository(ABC):
    def read(self):
        pass  # pragma: no cover

    def save(self, data: dict):
        pass  # pragma: no cover
