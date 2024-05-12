import random
import allure
from scooter_api import ScooterApi


class TestGetOrder:
    @allure.title('Проверка получения списка заказов')
    @allure.description("Проверяем получение списка заказов")
    def test_success_get_orders(self):
        get_order_response = ScooterApi.get_order()
        assert get_order_response.status_code == 200
        assert "orders" in get_order_response.json()

    @allure.title('Проверка получения списка заказов с невалидным курьером')
    @allure.description("Проверяем получение сообщения об ошибке при использовании случайных значений courierId")
    def test_get_order_with_invalid_courierId(self):
        random_courierId = random.randint(999999, 9999999)
        get_order_response = ScooterApi.get_order(courierId=random_courierId)
        assert get_order_response.status_code == 404
        assert f"Курьер с идентификатором {random_courierId} не найден" in get_order_response.json()["message"]
