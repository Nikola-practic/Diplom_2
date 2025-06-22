import requests
from data import *
from urls import *


class UserMethods:

    # Регистрация нового пользователя
    def register_new_user(self, user_data):
        return  requests.post(f"{Urls.MAIN_URL}{Urls.CREATE_USER}", json=user_data)

    # Авторизация пользователя
    def login_user(self, user_data):
        return requests.post(f"{Urls.MAIN_URL}{Urls.LOGIN}", json=user_data)

