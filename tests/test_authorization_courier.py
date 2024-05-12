import allure
from faker import Faker

from helper import CourierFactory
from scooter_api import ScooterApi


class TestAuthCourier:
    @allure.title('Проверка успешной авторизации курьера')
    @allure.description("Авторизация существующего курьера, проверка статуса ответа и тела ответа")
    def test_success_auth_courier(self, default_courier):
        _, auth_response, _, _ = default_courier
        assert auth_response.status_code == 200
        assert "id" in auth_response.json()
        assert len(str(auth_response.json()["id"])) == 6

    @allure.title('Неуспешная авторизация при запросе без логина')
    @allure.description("Авторизация не проходит, если не введен логин")
    def test_cannot_auth_courier_with_empty_login(self, default_courier):
        _, _, _, courier_pass = default_courier
        auth_courier_response_with_empty_login = ScooterApi.auth_courier({"login": "", "password": courier_pass})

        assert auth_courier_response_with_empty_login.status_code == 400 \
               and auth_courier_response_with_empty_login.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Неуспешная авторизация при запросе без пароля')
    @allure.description("Авторизация не проходит, если не введен пароль")
    def test_cannot_auth_courier_with_empty_pass(self, default_courier):
        _, _, courier_login, _ = default_courier
        auth_courier_response_with_empty_pass = ScooterApi.auth_courier({"login": courier_login, "password": ""})

        assert auth_courier_response_with_empty_pass.status_code == 400 \
               and auth_courier_response_with_empty_pass.json()["message"] == "Недостаточно данных для входа"

    @allure.title('Неуспешная авторизация при вводе невалидных данных')
    @allure.description("Проверка: нельзя авторизоваться, если ввести несуществующие данные")
    def test_cannot_auth_courier_with_invalid_login_and_pass(self):
        response = ScooterApi.auth_courier(CourierFactory.courier_body_with_random_data())
        assert response.status_code == 404 and response.json()["message"] == "Учетная запись не найдена"

    @allure.title('Неуспешная авторизация при вводе невалидного пароля')
    @allure.description("Авторизация не проходит, если ввести неверный пароль")
    def test_cannot_auth_courier_with_invalid_pass(self, default_courier):
        _, _, courier_login, _ = default_courier
        fake = Faker()
        fake_password = fake.name()
        auth_courier_response_with_invalid_pass = ScooterApi.auth_courier(
            {"login": courier_login, "password": fake_password})
        assert auth_courier_response_with_invalid_pass.status_code == 404\
               and auth_courier_response_with_invalid_pass.json()["message"] == "Учетная запись не найдена"

    @allure.title('Неуспешная авторизация при вводе невалидного логина')
    @allure.description("Авторизация не проходит, если авторизоваться под несуществующим пользователем")
    def test_cannot_auth_courier_with_invalid_login(self, default_courier):
        _, _, _, courier_pass = default_courier
        fake = Faker()
        fake_login = fake.name()
        auth_courier_response_with_invalid_login = ScooterApi.auth_courier(
            {"login": fake_login, "password": courier_pass})
        assert auth_courier_response_with_invalid_login.status_code == 404\
               and auth_courier_response_with_invalid_login.json()["message"] == "Учетная запись не найдена"
