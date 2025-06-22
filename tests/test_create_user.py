import pytest
import allure
import requests
from data import *
from conftest import *


@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя ')
    def test_create_new_user_success(self, user_methods):
        user = UsersData.create_user_data

        with allure.step('Отправляет запрос на регистрацию пользователя в системе'):
            response = user_methods.register_new_user(user)
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что в ответе возвращается тело, в том числе получение accessToken и refreshToken'):
            assert r['success'] is True
            assert 'accessToken' in r.keys()
            assert 'refreshToken' in r.keys()
            assert r['user']['email'] == user['email']
            assert r['user']['name'] == user['name']


    @allure.title('Создание пользователя, который уже зарегистрирован в системе')
    def test_create_double_user_error(self, user_methods):

        with allure.step('Создание первого пользователя'):
            user = UsersData.create_user_data
            user_methods.register_new_user(user)

        with allure.step('Пытаемся создать дубликат пользователя'):
            response = user_methods.register_new_user(user)
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 403'):
            assert response.status_code == 403

        with (allure.step('Проверяем сообщение об ошибке')):
            assert r.get("message") == Assertions.USER_ALREADY_EXISTS


    @allure.title('Создание пользователя с незаполненными обязательными полями')
    @pytest.mark.parametrize('credentials', UsersData.create_user_incorrect_data)
    def test_create_user_incorrect_data(self, user_methods, credentials):

        with allure.step('Отправка запроса на регистрацию пользователя'):
            response = user_methods.register_new_user(credentials)
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 403'):
            assert response.status_code == 403

        with allure.step('Проверяем сообщение об ошибке'):
            assert r.get("message") == Assertions.REQUIRED_FIELDS_MISSING

