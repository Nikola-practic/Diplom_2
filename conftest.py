import pytest
import allure
import requests
from generators import *
from methods.user_methods import UserMethods
from methods.order_methods import OrderMethods


@pytest.fixture()
def user_methods():
    return UserMethods()

@pytest.fixture()
def order_methods():
    return OrderMethods()

@pytest.fixture
@allure.title('Фикстура создает пользователя и удаляет его из базы после теста')
def create_new_user_and_delete():
    user = generate_user_data()
    yield user
    delete_user(user["accessToken"])

