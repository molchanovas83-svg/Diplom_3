import pytest
from selenium import webdriver
from data.urls import Urls
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage
from pages.profile_page import ProfilePage
from pages.feed_page import FeedPage
from pages.order_history_page import OrderHistoryPage


@pytest.fixture(params=["firefox", "chrome"])
def driver(request):
    browser_name = request.param
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    elif browser_name == "firefox":
        service = FirefoxService(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=service)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    driver.maximize_window()
    driver.get(Urls.MAIN_URL)
    yield driver
    driver.quit()


@pytest.fixture()
def main_page(driver):
    return MainPage(driver)


@pytest.fixture()
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture()
def forgot_page(driver):
    return ForgotPage(driver)


@pytest.fixture()
def profile_page(driver):
    return ProfilePage(driver)


@pytest.fixture()
def feed_page(driver):
    return FeedPage(driver)


@pytest.fixture()
def order_history_page(driver):
    return OrderHistoryPage(driver)
