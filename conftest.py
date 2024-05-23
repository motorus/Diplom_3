import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from helps import NewUserCreds, User
from pages.main_page import MainPage


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
        driver = webdriver.Firefox(options=options)
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

    main_page = MainPage(driver)
    main_page.login_user(new_user)




