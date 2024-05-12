import allure
import pytest
import helper
from scooter_api import ScooterApi


class TestCreateCourier:
    @allure.title('Проверка успешного создания курьера')
    @allure.description("Создание нового курьера, проверка статуса ответа и тела ответа")
    def test_success_create_courier(self, default_courier):
        courier_response, _, _, _ = default_courier
        assert courier_response.status_code == 201 and courier_response.json()["ok"] == True, "Ожидался ответ True"

    @allure.title('Создание курьера с уже существующим логином')
    @allure.description("Повторное создание курьера с тем же логином возвращает ошибку")
    def test_cannot_create_courier_with_existing_login(self, default_courier):
        _, _, courier_login, _ = default_courier
        second_courier_response = ScooterApi.create_courier({"login": courier_login, "password": "some_password"})
        assert second_courier_response.status_code == 409 \
               and second_courier_response.json()["message"] == "Этот логин уже используется. Попробуйте другой."

    @allure.title('Создание курьера c пустым логином')
    @allure.description("Создание курьера c пустым логином возвращает ошибку")
    def test_cannot_create_courier_with_empty_login(self):
        new_courier_data = helper.CourierFactory.courier_body_with_random_data()
        new_courier_data["login"] = ""
        response = ScooterApi.create_courier(new_courier_data)
        assert response.status_code == 400 \
               and response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Создание курьера c пустым паролем')
    @allure.description("Создание курьера c пустым паролем возвращает ошибку")
    @pytest.mark.parametrize("password", [
        pytest.param(' '),
        pytest.param('')
    ])
    def test_cannot_create_courier_with_empty_password(self, password):
        new_courier_data = helper.CourierFactory.courier_body_with_random_data()
        new_courier_data["password"] = password
        response = ScooterApi.create_courier(new_courier_data)
        assert response.status_code == 400 \
               and response.json()["message"] == "Недостаточно данных для создания учетной записи"

    @allure.title('Создание курьера c пустым именем')
    @allure.description("Успешное создание курьера c пустым именем")
    @pytest.mark.parametrize("firstName", [
        pytest.param(' '),
        pytest.param('')
    ])
    def test_success_create_courier_with_empty_firstname(self, firstName):
        new_courier_data = helper.CourierFactory.courier_body_with_random_data()
        new_courier_data["firstName"] = firstName
        response = ScooterApi.create_courier(new_courier_data)
        assert response.status_code == 201 \
               and response.json()["ok"] == True, "Ожидался ответ True"
