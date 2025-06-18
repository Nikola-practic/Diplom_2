class Urls:
    MAIN_URL = 'https://stellarburgers.nomoreparties.site'

    # Регистрация пользователя
    CREATE_USER = '/api/auth/register'

    # Авторизация пользователя
    LOGIN = '/api/auth/login'

    # Получение данных о пользователе
    #CHANGE_USER_DATA = '/api/auth/user'

    # Удаление пользователя
    DELETE_USER = '/api/auth/user'

    # Сделать заказ пользователем
    CREATE_ORDER = '/api/orders'

    headers = {'Content-Type': 'application/json'}
