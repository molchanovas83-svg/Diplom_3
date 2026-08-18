import allure
import pytest
from data.urls import Urls
from data.data import Credential
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.forgot_page_locators import ForgotPageLocators


class TestRecoveryPassword:
    @allure.title('Проверка восстановления пароля')
    def test_recovery(self, main_page: MainPage, login_page: LoginPage, forgot_page: ForgotPage):
        main_page.find_element(MainPageLocators.ACCOUNT_BUTTON).click()

        # переход на страницу восстановления пароля по кнопке «Восстановить пароль»
        login_page.find_element(LoginPageLocators.FORGOT_PASSWORD_BUTTON).click()
        assert Urls.FORGOT_PASSWORD_URL == login_page.get_current_url()

        # ввод почты и клик по кнопке «Восстановить»
        forgot_page.find_element(ForgotPageLocators.EMAIL_INPUT).send_keys(Credential.email)
        forgot_page.find_element(ForgotPageLocators.RECOVERY_BUTTON).click()

        # клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.
        forgot_page.find_element(ForgotPageLocators.PASSWORD_ICON).click()
        forgot_page.find_element(ForgotPageLocators.PASSWORD_ACTIVE)

