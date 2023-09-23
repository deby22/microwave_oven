from microwave.application.schemas import Microwave as MicrowaveDTO
from microwave.application.service import ApplicationService
from microwave.infrastructure.repositories.in_memory import InMemoryRepository


class TestGetState:
    def test_get_state_with_initial_state(self):
        service = ApplicationService(repo=InMemoryRepository())
        assert service.get_state() == MicrowaveDTO(counter=0, power=0, state="OFF")


class TestUpdatePower:
    def test_increase_power_should_update_power(self):
        service = ApplicationService(repo=InMemoryRepository())
        service.update_power(10)
        assert service.get_state() == MicrowaveDTO(counter=0, power=10, state="ON")

    def test_decrease_power_should_update_power(self):
        service = ApplicationService(repo=InMemoryRepository())
        service.update_power(10)
        service.update_power(-5)
        assert service.get_state() == MicrowaveDTO(counter=0, power=5, state="ON")


class TestUpdateTime:
    def test_increase_time_should_update_time(self):
        service = ApplicationService(repo=InMemoryRepository())
        service.update_counter(10)
        assert service.get_state() == MicrowaveDTO(counter=10, power=0, state="ON")

    def test_decrease_time_should_update_time(self):
        service = ApplicationService(repo=InMemoryRepository())
        service.update_counter(10)
        service.update_counter(-5)
        assert service.get_state() == MicrowaveDTO(counter=5, power=0, state="ON")


class TestCancel:
    def test_cancel_should_clear_all_values(self):
        service = ApplicationService(repo=InMemoryRepository())
        service.update_counter(10)
        service.update_power(10)
        service.cancel()
        assert service.get_state() == MicrowaveDTO(counter=0, power=0, state="OFF")
