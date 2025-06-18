import pytest
import allure
import requests
from data import *
from  urls import *


@allure.suite('Создание пользователя')
class TestCreateUser:

    @allure.title('Создание уникального пользователя ')
    def test_create_new_user_success(self):

        with allure.step('Генерируем данные для нового пользователя'):
            payload = {
                'email': create_random_email(),
                'password': create_random_password(),
                'name': create_random_username()
            }
        with allure.step('Отправляет запрос на регистрацию пользователя в системе'):
            response = requests.post(f'{Urls.MAIN_URL}{Urls.CREATE_USER}', data=payload)
            r = response.json()

        with allure.step('Проверяем, что возвращается код ответа 200'):
            assert response.status_code == 200

        with allure.step('Проверяем, что в ответе возвращается тело, в том числе получение accessToken и refreshToken'):
            assert r['success'] is True
            assert 'accessToken' in r.keys()
            assert 'refreshToken' in r.keys()
            assert r['user']['email'] == payload['email']
            assert r['user']['name'] == payload['name']

        with allure.step('Удаление использованных тестовых данных из базы после теста'):
            access_token = r['accessToken']
            requests.delete(f"{Urls.MAIN_URL}{Urls.DELETE_USER}", headers={'Authorization': access_token})


    @allure.title('Создание пользователя, который уже зарегистрирован в системе')
    def test_create_double_user_error(self):

        with allure.step('Задаём данные для нового пользователя'):
            payload = {
                'email': UsersData.email,
                'password': UsersData.password,
                'name': UsersData.username
            }
        with allure.step('Создание первого пользователя'):
            requests.post(f'{Urls.MAIN_URL}{Urls.CREATE_USER}', json=payload)

        with allure.step('Пытаемся создать дубликат пользователя'):
            response = requests.post(f'{Urls.MAIN_URL}{Urls.CREATE_USER}', json=payload)

        with allure.step('Проверяем, что возвращается код ответа 403'):
            assert response.status_code == 403

        with (allure.step('Проверяем сообщение об ошибке')):
            assert response.json() == {'success': False, 'message':'User already exists'}


    @allure.title('Создание пользователя с незаполненными обязательными полями')
    @pytest.mark.parametrize('credentials', UsersData.create_user_incorrect_data)
    def test_create_user_incorrect_data(self, credentials):

        with allure.step('Отправка запроса на регистрацию пользователя'):
            response = requests.post(f'{Urls.MAIN_URL}{Urls.CREATE_USER}', data=credentials)

        with allure.step('Проверяем, что возвращается код ответа 403'):
            assert response.status_code == 403

        with allure.step('Проверяем сообщение об ошибке'):
            assert  response.json() == {'success': False, 'message': 'Email, password and name are required fields'}

