import allure
import pytest
from data.urls import Urls
from data.data import Credential
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage
from pages.profile_page import ProfilePage
from pages.feed_page import FeedPage
from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators


class TestFunctionality:
    @allure.title('Проверка основного функционала')
    def test_functionality(
            self,
            main_page: MainPage,
            login_page: LoginPage,
            profile_page: ProfilePage,
    ):
        # переход по клику на «Лента заказов»,
        main_page.find_element(MainPageLocators.ORDER_FEED_BUTTON).click()
        assert Urls.FEED_URL == profile_page.get_current_url()

        # переход по клику на «Конструктор»,
        main_page.find_element(MainPageLocators.CONSTRUCTOR_BUTTON).click()
        assert Urls.MAIN_URL == profile_page.get_current_url()

        # если кликнуть на ингредиент, появится всплывающее окно с деталями
        main_page.find_element(MainPageLocators.INGREDIENTS).click()
        main_page.find_element(MainPageLocators.INGREDIENTS_MODAL)

        # всплывающее окно закрывается кликом по крестику,
        main_page.find_element(MainPageLocators.CLOSE_MODAL_BUTTON).click()
        main_page.wait_invisibility(MainPageLocators.INGREDIENTS_MODAL)

        # при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента
        assert main_page.find_element(MainPageLocators.COUNTER_INGREDIENT).text == '0'
        main_page.drag_and_drop(MainPageLocators.INGREDIENTS, MainPageLocators.BURGER_CONSTRUCTOR)
        assert main_page.find_element(MainPageLocators.COUNTER_INGREDIENT).text == '2'

        # залогиненный пользователь может оформить заказ.
        main_page.find_element(MainPageLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        login_page.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(Credential.email)
        login_page.find_element(LoginPageLocators.EMAIL_PASSWORD).send_keys(Credential.password)
        login_page.find_element(LoginPageLocators.ENTER_BUTTON).click()
        main_page.find_element(MainPageLocators.CREATE_ORDER_BUTTON)

