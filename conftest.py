import pytest
import allure
import requests
from urls import *
from data import *


@pytest.fixture
@allure.title('Фикстура создает пользователя с рандомными данными и удаляет его из базы после теста')
def create_new_user_and_delete():
    payload_create = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()
    }
    response = requests.post(f"{Urls.MAIN_URL}{Urls.CREATE_USER}", data=payload_create)
    response_body = response.json()

    yield payload_create, response_body

    access_token = response_body['accessToken']
    requests.delete(f"{Urls.MAIN_URL}{Urls.DELETE_USER}", headers={'Authorization': access_token})
