from helpers import *

class UsersData:
    create_user_data = {
        'email': create_random_email(),
        'password': create_random_password(),
        'name': create_random_username()
    }

    duplicate_user = {
        "email": "ivanov2169@yandex.ru",
        "password": "ivan2169",
        "username": "Ivanov2169"
    }

    create_user_incorrect_data = [
        {'email': '',
         'password': create_random_password(),
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': '',
         'name': create_random_username()
         },
        {'email': create_random_email(),
         'password': create_random_password(),
         'name': ''
         }
    ]

class IngredientData:
    burger_1 = ["61c0c5a71d1f82001bdaaa73",
                "61c0c5a71d1f82001bdaaa76", "61c0c5a71d1f82001bdaaa79"]

    burger_2 = ["61c0c5a71d1f82001bdaaa71", "61c0c5a71d1f82001bdaaa74"]

    invalid_hash_ingredient = ["60d3b41abdacab0026a733c6g"]


class Assertions:

    INGREDIENTS_REQUIRED = "Ingredient ids must be provided"

    INTERNAL_SERVER_ERROR_TEXTS = "Internal Server Error"

    LOGIN_INCORRECT_MESSAGE = "email or password are incorrect"

    USER_ALREADY_EXISTS = "User already exists"

    REQUIRED_FIELDS_MISSING = "Email, password and name are required fields"

    #USER_NOT_AUTHORIZED = "You should be authorised"
