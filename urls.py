class URLS:

    MAIN = 'https://stellarburgers.nomoreparties.site/'  # главная страница
    #REG = 'https://stellarburgers.nomoreparties.site/register'  # регистрация
    #LOGIN = 'https://stellarburgers.nomoreparties.site/login'  # авторизация
    #FORGOT_PASS = 'https://stellarburgers.nomoreparties.site/forgot-password'  # восстановление пароля
    #RESET_PASS = 'https://stellarburgers.nomoreparties.site/reset-password'  # восстановление пароля
    #PERSONAL_AREA = 'https://stellarburgers.nomoreparties.site/account/profile'
    #ORDER_HISTORY = 'https://stellarburgers.nomoreparties.site/account/order-history'
    #ORDER_FEED = 'https://stellarburgers.nomoreparties.site/feed'

    REG         = MAIN + 'register'  # регистрация
    LOGIN       = MAIN + 'login'  # авторизация
    FORGOT_PASS = MAIN + 'forgot-password'  # восстановление пароля
    RESET_PASS  = MAIN + 'reset-password'  # восстановление пароля
    PERSONAL_AREA = MAIN + 'account/profile'
    ORDER_HISTORY = MAIN + 'account/order-history'
    ORDER_FEED  = MAIN + 'feed'


class EndPoints:
    test_url = 'https://stellarburgers.nomoreparties.site'
    ingridients     = test_url + '/api/ingredients'  # get
    create_order    = test_url + '/api/orders'  # post {"ingredients": ["123123123","456456456"]}
    create_user     = test_url + '/api/auth/register'  # post {"email": "test-data@yandex.ru",
                                                   # "password": "password",
                                                   # "name": "Username"}
    login_user      = test_url + '/api/auth/login'  # post
    get_user_info   = test_url + '/api/auth/user'  # GET    Оставил список таким потому что так удобнее
    update_user     = test_url + '/api/auth/user'  # PATCH
    delete_user     = test_url + '/api/auth/user'  # DELETE
    get_all_orders  = test_url + '/api/orders/all'  # GET
    get_orders      = test_url + '/api/orders'  # GET
