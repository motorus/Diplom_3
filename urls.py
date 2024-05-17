from datetime import datetime


class URLS:

    MAIN = 'https://stellarburgers.nomoreparties.site/'  # главная страница
    REG = 'https://stellarburgers.nomoreparties.site/register'  # регистрация
    LOGIN = 'https://stellarburgers.nomoreparties.site/login'  # авторизация
    FORGOT_PASS = 'https://stellarburgers.nomoreparties.site/forgot-password'  # восстановление пароля
    RESET_PASS = 'https://stellarburgers.nomoreparties.site/reset-password'  # восстановление пароля
    PERSONAL_AREA = 'https://stellarburgers.nomoreparties.site/account/profile'
    ORDER_HISTORY = 'https://stellarburgers.nomoreparties.site/account/order-history'
    ORDER_FEED = 'https://stellarburgers.nomoreparties.site/feed'


class EndPoints:
    test_url = 'https://stellarburgers.nomoreparties.site'
    ingridients = test_url + '/api/ingredients'  # get

    create_order = test_url + '/api/orders'  # post {"ingredients": ["60d3b41abdacab0026a733c6","609646e4dc916e00276b2870"]}

    password_recovery = test_url + 'api/password-reset'  # post {"email": ""}

    create_user = test_url + '/api/auth/register'  # post {"email": "test-data@yandex.ru",
    # "password": "password",
    # "name": "Username"}

    login_user = test_url + '/api/auth/login'  # post {"email": "",
    # "password": ""}

    get_user_info = test_url + '/api/auth/user'  # GET
    update_user = test_url + '/api/auth/user'  # PATCH
    delete_user = test_url + '/api/auth/user'  # DELETE

    get_all_orders = test_url + '/api/orders/all'  # GET
    get_orders = test_url + '/api/orders'  # GET
