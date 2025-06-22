import requests
from data import *
from urls import *


class OrderMethods:
    # Запрос на создание заказа c авторизацией
    def create_order(self, ingredients, token=None):
        headers = {"Authorization": token} if token else {}
        return requests.post(f"{Urls.MAIN_URL}{Urls.CREATE_ORDER}",  headers=headers, json={"ingredients": ingredients})

    # Запрос на создание заказа без авторизации
    def create_orders_not_avtorized(self, ingredients):
        headers = Urls.headers
        return requests.post(f"{Urls.MAIN_URL}{Urls.CREATE_ORDER}", headers=headers, json={"ingredients": ingredients})



