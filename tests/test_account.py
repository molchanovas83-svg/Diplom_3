import allure
import pytest
from data.urls import Urls
from data.data import Credential
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage
from pages.profile_page import ProfilePage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators


class TestAccount:
    @allure.title('Проверка личного кабинета')
    def test_account(
            self, main_page: MainPage, login_page: LoginPage, forgot_page: ForgotPage, profile_page: ProfilePage):
        # переход по клику на «Личный кабинет»
        main_page.find_element(MainPageLocators.ACCOUNT_BUTTON).click()
        login_page.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(Credential.email)
        login_page.find_element(LoginPageLocators.EMAIL_PASSWORD).send_keys(Credential.password)
        login_page.find_element(LoginPageLocators.ENTER_BUTTON).click()
        main_page.find_element(MainPageLocators.ACCOUNT_BUTTON).click()

        # переход в раздел «История заказов»
        profile_page.find_element(ProfilePageLocators.HISTORY_BUTTON).click()
        assert Urls.ORDER_HISTORY_URL in profile_page.get_current_url()

        # выход из аккаунта
        profile_page.find_element(ProfilePageLocators.EXIT_BUTTON).click()
        assert Urls.LOGIN_URL == profile_page.get_current_url()


