import requests
from urls import Urls
from helpers import *


def generate_user_data():
    email = create_random_email()
    password = create_random_password()
    name = create_random_username()
    data = {"email": email, "password": password, "name": name}
    response = requests.post(f"{Urls.MAIN_URL}{Urls.CREATE_USER}", json=data)
    response.raise_for_status()
    result = response.json()
    return {
        "email": email,
        "password": password,
        "name": name,
        "accessToken": result["accessToken"],
        "refreshToken": result["refreshToken"]
    }

def delete_user(token):
    if token:
        headers = {"Authorization": token}
        requests.delete(f"{Urls.MAIN_URL}{Urls.DELETE_USER}", headers=headers)