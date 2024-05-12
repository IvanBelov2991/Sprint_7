import allure
import requests
import urls


class ScooterApi:

    @staticmethod
    @allure.step('Отправка запроса на создание курьера')
    def create_courier(body):
        return requests.post(urls.BASE_URL + urls.CREATE_COURIER_ENDPOINT, json=body)

    @staticmethod
    @allure.step('Отправка запроса на авторизацию курьера')
    def auth_courier(body):
        return requests.post(urls.BASE_URL + urls.AUTH_COURIER_ENDPOINT, json=body)

    @staticmethod
    @allure.step('Отправка запроса на удаление курьера')
    def delete_courier(courier_id):
        delete_requests = requests.delete(urls.BASE_URL + urls.DELETE_COURIER_ENDPOINT + str(courier_id))
        return delete_requests

    @staticmethod
    @allure.step('Отправка запроса на создание заказа')
    def create_order(body):
        order_requests = requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=body)
        return order_requests

    @staticmethod
    @allure.step('Отправка запроса на получение заказов')
    def get_order(courierId=None):
        if courierId:
            endpoint = f"{urls.GET_ORDER_ENDPOINT}?courierId={courierId}"
        else:
            endpoint = urls.GET_ORDER_ENDPOINT
        get_requests = requests.get(urls.BASE_URL + endpoint)
        return get_requests

