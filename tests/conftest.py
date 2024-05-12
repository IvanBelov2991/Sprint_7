import allure
import pytest

import helper
from scooter_api import ScooterApi


@allure.step("Создание нового курьера и удаление данных после завершения теста")
@pytest.fixture(scope='function')
def default_courier():
    data = helper.CourierFactory.courier_body_with_random_data()
    courier_response = ScooterApi.create_courier(data)

    courier_login = data["login"]
    courier_pass = data["password"]
    auth_response = ScooterApi.auth_courier({"login": courier_login, "password": courier_pass})

    yield courier_response, auth_response, courier_login, courier_pass

    courier_id = auth_response.json()["id"]
    ScooterApi.delete_courier(courier_id)
