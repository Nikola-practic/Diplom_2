import pytest
import allure
import requests
from data import *


@allure.suite('Создание заказа')
class TestCreateOrder:

    @allure.title('Создание заказа авторизованным пользователем с ингредиентами')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_create_order_authorized_with_ingredients(self, order_methods, create_new_user_and_delete, burger_ingredients):

        with (allure.step('Отправляем запрос на создание заказа')):
            response = order_methods.create_order(burger_ingredients, create_new_user_and_delete["accessToken"])
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что в ответе возвращается тело'):
            assert r["success"] is True
            assert "name" in r.keys()
            assert "number" in r["order"].keys()


    @allure.title('Создание заказа не авторизованным пользователем с ингредиентами')
    @pytest.mark.parametrize('burger_ingredients', [IngredientData.burger_1, IngredientData.burger_2])
    def test_create_order_not_authorized_with_ingredients(self, order_methods, burger_ingredients):

        with allure.step('Отправляет запрос на создание заказа'):
            response = order_methods.create_orders_not_avtorized(burger_ingredients)
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что в ответе возвращается тело'):
            assert r["success"] is True
            assert "name" in r.keys()
            assert "number" in r["order"].keys()


    @allure.title('Создание заказа авторизованным пользователем без ингредиентов')
    def test_create_order_authorized_no_ingredients(self, order_methods, create_new_user_and_delete):

        with allure.step('Отправляет запрос на создание заказа без ингредиентов'):
            response = order_methods.create_order([], create_new_user_and_delete["accessToken"])
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 400'):
            assert response.status_code == 400

        with allure.step('Проверяем, что в ответе возвращается сообщение об ошибке'):
            assert r.get("message") == Assertions.INGREDIENTS_REQUIRED


    @allure.title('Создание заказа с неверным хешем ингредиентов')
    def test_create_order_invalid_hash_ingredient(self, order_methods, create_new_user_and_delete):

        with allure.step('Отправляет запрос на создание заказа с невалидным хешем ингредиента'):
            response = order_methods.create_order(IngredientData.invalid_hash_ingredient, create_new_user_and_delete["accessToken"])

        with allure.step('Проверяем, что возвращается код ответа 500'):
            assert response.status_code == 500

            assert Assertions.INTERNAL_SERVER_ERROR_TEXTS in response.text






