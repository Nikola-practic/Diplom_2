
## Дипломный проект. Задание 2: Автотесты для API
<hr>

## Студент: Николай Яцына

## <h>Когорта: #21</h>
<hr>

### Автотесты эндпоинтов API для Stellar Burgers https://stellarburgers.nomoreparties.site/

### Документация API https://code.s3.yandex.net/qa-automation-engineer//python-full/diploma/api-documentation.pdf?etag=3403196b527ca03259bfd0cb41163a89

### Реализованные сценарии

**Создание пользователя (файл 'test_create_user.py'):**
- создание уникального пользователя;
- создание пользователя, который уже зарегистрирован; 
- создание пользователя и не заполнением одного из обязательных полей.

**Логин пользователя (файл 'test_login_user.py'):**
- вход под существующим пользователем;
- вход с неверным логином и паролем.

**Создание заказа (файл 'test_create_order.py):**
- с авторизацией;
- без авторизации;
- с ингредиентами;
- без ингредиентов;
- с неверным хешем ингредиентов.

### Структура проекта

Все тесты -> в пакете 'tests'

Фикстуры -> в файле 'conftest.py'

Все URLS -> в файле 'urls.py'

- `praktikum` - пакет, содержащий код программы
- `tests` - пакет, содержащий тесты, разделенные по классам: 
`test_bun.py`, `test_burger.py`, `test_ingredient.py`, `test_database.py`, `test_ingredient_types.py`

### Запуск автотестов

**Установка зависимостей**

>  pip install -r requirements.txt

**Запуск автотестов и создание HTML-отчета о покрытии**

>  pytest test --alluredir=allure_results
> 
> **Посмотреть отчёт в веб версии пройденного прогона**
> 
>  allure serve allure_results
