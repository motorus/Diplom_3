import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service

from locators.login_page_locators import LoginLocators

from helps import NewUserCreds, User
from urls import URLS
"""
@pytest.fixture(scope='function')
def driver():

    options = ChromeOptions()
    options.add_argument('--windows-size=1024,768')
    driver1 = webdriver.Chrome(options=options)
    driver1.maximize_window()

    yield driver1
    driver1.quit()
"""

@pytest.fixture(scope='function', params=["chrome", "firefox"])
def driver(request):
    driver = ""
    if request.param == "chrome":
        options = ChromeOptions()
        options.add_argument('--windows-size=1024,768')
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
    elif request.param == "firefox":
        options = FirefoxOptions()
        options.add_argument('--windows-size=1024,768')
        service = Service(executable_path='/home/user/Downloads/WebDriver/geckodriver') # убрать перед реквестом
        driver = webdriver.Firefox(options=options, service=service)
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def new_user():
    new_user_creds = NewUserCreds.generate_creds_set()
    new_user_response = User.create_user(new_user_creds)

    yield new_user_response, new_user_creds
    User.delete_user(new_user_response.json()["accessToken"])


@pytest.fixture(scope='function')
def logged_driver(driver, new_user):
    driver.get(URLS.LOGIN)

    driver.find_element(*LoginLocators.EMAIL_FIELD).send_keys(new_user[1]["email"])
    driver.find_element(*LoginLocators.PASSWORD_FIELD).send_keys(new_user[1]["password"])

    element = driver.find_element(*LoginLocators.ENTER_BUTTON)
    driver.execute_script("arguments[0].click();", element)  # костыль для прохождения тестов на ФФ

    yield driver
    driver.quit()
