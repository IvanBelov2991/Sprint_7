import random
import allure
from faker import Faker


class CourierFactory:
    @staticmethod
    @allure.step("Генерация body для создания курьера")
    def courier_body_with_random_data():
        fake = Faker()

        return {
            "login": fake.name(),
            "password": str(random.randint(0, 9999)),
            "firstName": fake.name()
        }
