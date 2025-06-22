import pytest
import allure
import requests
from urls import *
from data import *


@allure.suite('Логин пользователя')
class TestRegistration:

    @allure.title('Вход под существующим пользователем')
    def test_login_user(self, user_methods, create_new_user_and_delete):
        payload = {"email": create_new_user_and_delete["email"], "password": create_new_user_and_delete["password"]}

        with allure.step('Отправляет запрос на авторизацию пользователя, который есть в системе'):
            response = user_methods.login_user(payload)
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что в ответе возвращается тело, в том числе получение accessToken и refreshToken'):
            assert r['success'] is True
            assert 'accessToken' in r.keys()
            assert 'refreshToken' in r.keys()


    @allure.title('Вход с неверным логином')
    def test_login_user_error(self, user_methods, create_new_user_and_delete):
        payload = {"email": create_new_user_and_delete["email"], "password": "password"}

        with allure.step('Отправляет запрос на авторизацию пользователя c некорректным логином'):
            response = user_methods.login_user(payload)
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 401'):
            assert response.status_code == 401

        with allure.step('Проверяем, что в ответе возвращается сообщение об ошибке'):
            assert r.get("message") == Assertions.LOGIN_INCORRECT_MESSAGE


    @allure.title('Вход с неверным паролем')
    def test_password_user_error(self, user_methods, create_new_user_and_delete):
        payload = {"email": "email", "password": create_new_user_and_delete["password"]}

        with allure.step('Отправляет запрос на авторизацию пользователя c некорректным паролем'):
            response = user_methods.login_user(payload)
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 401'):
            assert response.status_code == 401

        with allure.step('Проверяем, что в ответе возвращается сообщение об ошибке'):
            assert r.get("message") == Assertions.LOGIN_INCORRECT_MESSAGE

