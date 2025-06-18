import pytest
import allure
import requests
from data import *
from urls import *


@allure.suite('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем с ингредиентами')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_create_order_authorized_with_ingredients(self, create_new_user_and_delete, burger_ingredients):
        headers = {"Authorization": create_new_user_and_delete[1]["accessToken"]}
        payload = {"ingredients": [burger_ingredients]}

        with allure.step('Отправляем запрос на создание заказа'):
            response = requests.post(f"{Urls.MAIN_URL}{Urls.CREATE_ORDER}",  data=payload, headers=headers)
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что в ответе возвращается тело'):
            assert r["success"] is True
            assert "name" in r.keys()
            assert "number" in r["order"].keys()


    @allure.title('Создание заказа не авторизованным пользователем с ингредиентами')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_create_order_not_authorized_with_ingredients(self, burger_ingredients):
        payload = {"ingredients": [burger_ingredients]}

        with allure.step('Отправляет запрос на создание заказа'):
            response = requests.post(f"{Urls.MAIN_URL}{Urls.CREATE_ORDER}", data=payload, headers=Urls.headers)

        with allure.step('Проверяем, что возвращается код ответа 400'):
            assert response.status_code == 400


    @allure.title('Создание заказа авторизованным пользователем без ингредиентов')
    def test_create_order_authorized_no_ingredients(self, create_new_user_and_delete):
        headers = {"Authorization": create_new_user_and_delete[1]["accessToken"]}
        payload = {"ingredients": []}

        with allure.step('Отправляет запрос на создание заказа без ингредиентов'):
            response = requests.post(f"{Urls.MAIN_URL}{Urls.CREATE_ORDER}", data=payload, headers=headers)

        with allure.step('Проверяем, что возвращается код ответа 400'):
            assert response.status_code == 400

        with allure.step('Проверяем, что в ответе возвращается сообщение об ошибке'):
            assert response.json() == {"success": False, "message": "Ingredient ids must be provided"}


    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_hash_ingredient(self, create_new_user_and_delete):
        headers = {"Authorization": create_new_user_and_delete[1]["accessToken"]}
        payload = {"ingredients": IngredientData.invalid_hash_ingredient}

        with allure.step('Отправляет запрос на создание заказа с невалидным хешем ингредиента'):
            response = requests.post(f"{Urls.MAIN_URL}{Urls.CREATE_ORDER}", data=payload, headers=headers)

        with allure.step('Проверяем, что возвращается код ответа 500'):
            assert response.status_code == 500






