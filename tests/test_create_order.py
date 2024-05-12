import allure
import pytest
from data import order_test_data
from scooter_api import ScooterApi


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа')
    @allure.description("Проверяем успешное создание заказа c различными тестовыми данными:"
                        " цвет самоката BLACK, GREY, BLACK и GREY, без цвета")
    @pytest.mark.parametrize("order_data", order_test_data)
    def test_success_create_courier(self, order_data):
        order_response = ScooterApi.create_order(order_data)
        assert order_response.status_code == 201
        assert "track" in order_response.json()
