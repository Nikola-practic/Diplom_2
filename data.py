from helpers import *

class UsersData:
    email = 'nikolaivanov2169@yandex.ru'
    password = 'nik21'
    username = 'NikolaIvanov2169'

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
    burger_1 = ['61c0c5a71d1f82001bdaaa73',
                '61c0c5a71d1f82001bdaaa76', '61c0c5a71d1f82001bdaaa79']

    burger_2 = ['61c0c5a71d1f82001bdaaa71', '61c0c5a71d1f82001bdaaa74']

    invalid_hash_ingredient = ["60d3b41abdacab0026a733c6g"]