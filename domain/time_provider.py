import time
from abc import ABC


class TimeProvider(ABC):
    def get_current_time(self):
        pass  # pragma: no cover


class RealTimeProvider(TimeProvider):
    def get_current_time(self):
        return time.time()
