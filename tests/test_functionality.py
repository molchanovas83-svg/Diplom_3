import allure
import pytest
from data.urls import Urls
from data.data import Credential
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators


class TestFunctionality:
    @allure.title('Проверка перехода на «Ленту заказов»')
    def test_open_feed(self, main_page: MainPage, profile_page: ProfilePage):
        main_page.find_element(MainPageLocators.ORDER_FEED_BUTTON).click()
        assert Urls.FEED_URL == profile_page.get_current_url()

    @allure.title('Проверка перехода на «Конструктор»')
    def test_open_constructor(self, main_page: MainPage, profile_page: ProfilePage):
        main_page.find_element(MainPageLocators.CONSTRUCTOR_BUTTON).click()
        assert Urls.MAIN_URL == profile_page.get_current_url()

    @allure.title('Проверка всплывающего окна ингредиентов')
    def test_ingredient_window(self, main_page: MainPage, profile_page: ProfilePage):
        # если кликнуть на ингредиент, появится всплывающее окно с деталями
        main_page.find_element(MainPageLocators.INGREDIENTS).click()
        main_page.find_element(MainPageLocators.INGREDIENTS_MODAL)

        # всплывающее окно закрывается кликом по крестику,
        main_page.find_element(MainPageLocators.CLOSE_MODAL_BUTTON).click()
        main_page.wait_invisibility(MainPageLocators.INGREDIENTS_MODAL)

    @allure.title('Проверка что при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_increase_counter(self, main_page: MainPage, profile_page: ProfilePage):
        assert main_page.find_element(MainPageLocators.COUNTER_INGREDIENT).text == '0'
        main_page.drag_and_drop(MainPageLocators.INGREDIENTS, MainPageLocators.BURGER_CONSTRUCTOR)
        assert main_page.find_element(MainPageLocators.COUNTER_INGREDIENT).text == '2'

    @allure.title('Проверка что залогиненный пользователь может оформить заказ')
    def test_login_user_create_order(self, main_page: MainPage, profile_page: ProfilePage, login_page: LoginPage):
        main_page.find_element(MainPageLocators.ENTER_TO_ACCOUNT_BUTTON).click()
        login_page.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(Credential.email)
        login_page.find_element(LoginPageLocators.EMAIL_PASSWORD).send_keys(Credential.password)
        login_page.find_element(LoginPageLocators.ENTER_BUTTON).click()
        main_page.find_element(MainPageLocators.CREATE_ORDER_BUTTON)

