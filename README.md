## Дипломный проект. Задание 3: Тесты для веб страницы https://stellarburgers.nomoreparties.site


### Структура проекта

- allure_results/ - результаты запуска тестов allure
- conftest.py - фикстуры с драйвером для входа на сайт
- helps.py - вспомогательные классы и методы 
- locators/account_page_locators.py - локаторы личного кабинета
- locators/feed_page_locators.py - локаторы ленты заказов
- locators/login_page_locators.py - локаторы страницы логина
- locators/main_page_locators.py - локаторы главной страницы
- locators/password_locators.py - локаторы восстановления пароля

- pages/base_page.py - базовые методы
- pages/account_page.py - методы тестирования личного кабинета
- pages/login_page.py - методы тестирования страницы авторизации
- pages/main_page.py - методы тестирования главной страницы
- pages/order_feed_page.py - методы тестирования страницы заказов
- pages/password_pages.py - методы тестирования страницы восставления пароля

- tests/test_account_page.py - тесты личного кабинета
- tests/test_login_page.py - тесты авторизации
- tests/test_main_page.py - тесты главной страницы
- tests/test_order_feed.py - тесты ленты заказов
- tests/test_password_page.py - тесты страницы восстаноления пароля

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

#### Запуск тестов
`pytest tests/ --alluredir=allure_results`
#### Запуск отчетности allure
`allure serve allure_results`
