import pytest
import requests


@pytest.mark.integration
def test_read_updated_state():
    url = "http://localhost:8000"
    power = 25
    time = 10
    token = _given_token_has_been_created(url)
    _given_microwave_has_been_restarted(token, url)
    _given_power_has_been_increased(url, power)
    _given_time_has_been_increased(url, time)
    response = _when_state_has_been_fetched(url)
    assert _then_microwave_is_turn_on(response, power, time)


def _then_microwave_is_turn_on(response, power, time):
    return response == {'counter': time, 'power': power, 'state': 'ON'}


def _when_state_has_been_fetched(url):
    return requests.get(f"{url}/state").json()


def _given_time_has_been_increased(url, time):
    requests.post(f"{url}/time", json={"time": time})


def _given_power_has_been_increased(url, power):
    requests.post(f"{url}/power", json={"power": power})


def _given_microwave_has_been_restarted(token, url):
    requests.post(f"{url}/cancel", headers={"Authorization": f"Bearer {token}"})


def _given_token_has_been_created(url):
    return requests.post(f"{url}/signup", json={"email": "sample@email.com"}).json()


