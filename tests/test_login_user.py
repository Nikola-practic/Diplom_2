import pytest
import allure
import requests
from urls import *
from data import *


@allure.suite('Логин пользователя')
class TestRegistration:

    @allure.title('Вход под существующим пользователем')
    def test_login_user(self, create_new_user_and_delete):
        payload = create_new_user_and_delete[0]

        with allure.step('Отправляет запрос на авторизацию пользователя, который есть в системе'):
            response = requests.post(f'{Urls.MAIN_URL}{Urls.LOGIN}', data=payload)
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что в ответе возвращается тело, в том числе получение accessToken и refreshToken'):
            assert r['success'] is True
            assert 'accessToken' in r.keys()
            assert 'refreshToken' in r.keys()
            assert r['user']['email'] == payload['email']
            assert r['user']['name'] == payload['name']


    @allure.title('Вход с неверным логином')
    def test_login_user_error(self):
        payload = {
            'email': create_random_email(),
            'password': UsersData.password
        }

        with allure.step('Отправляет запрос на авторизацию пользователя c некорректным логином'):
            response = requests.post(f'{Urls.MAIN_URL}{Urls.LOGIN}', data=payload)

        with allure.step('Проверяем, что возвращается код ответа 401'):
            assert response.status_code == 401

        with allure.step('Проверяем, что в ответе возвращается сообщение об ошибке'):
            assert response.json() == {'success': False, 'message': 'email or password are incorrect'}


    @allure.title('Вход с неверным паролем')
    def test_password_user_error(self):
        payload = {
            'email': UsersData.email,
            'password': create_random_password(),
        }
        with allure.step('Отправляет запрос на авторизацию пользователя c некорректным паролем'):
            response = requests.post(f'{Urls.MAIN_URL}{Urls.LOGIN}', data=payload)

        with allure.step('Проверяем, что возвращается код ответа 401'):
            assert response.status_code == 401

        with allure.step('Проверяем, что в ответе возвращается сообщение об ошибке'):
            assert response.json().get("success") is False

