import allure
from data.urls import Urls
from data.data import Credential
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.forgot_page import ForgotPage
from pages.profile_page import ProfilePage
from pages.feed_page import FeedPage
from pages.order_history_page import OrderHistoryPage
from locators.main_page_locators import MainPageLocators
from locators.feed_page_locators import FeedPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.profile_page_locators import ProfilePageLocators


class TestFeed:
    @allure.title('Проверка ленты заказов')
    def test_open_feed(self, main_page: MainPage, feed_page: FeedPage, profile_page: ProfilePage):
        # переход по клику на «Лента заказов»,
        main_page.find_element(MainPageLocators.ORDER_FEED_BUTTON).click()
        assert Urls.FEED_URL == profile_page.get_current_url()

        # если кликнуть на заказ, откроется всплывающее окно с деталями
        feed_page.find_element(FeedPageLocators.ORDER).click()
        feed_page.find_element(FeedPageLocators.ORDER_FEED_MODAL)

        # всплывающее окно закрывается кликом по крестику,
        feed_page.find_element(FeedPageLocators.CLOSE_FEED_MODAL_BUTTON).click()
        feed_page.wait_invisibility(FeedPageLocators.ORDER_FEED_MODAL)

    @allure.title('Проверка что заказы пользователя из «Истории заказов» отображаются на странице «Лента заказов»')
    def test_user_orders(
            self,
            main_page: MainPage,
            login_page: LoginPage,
            profile_page: ProfilePage,
            order_history_page: OrderHistoryPage,
            feed_page: FeedPage
    ):
        # Авторизуемся
        main_page.find_element(MainPageLocators.ACCOUNT_BUTTON).click()
        login_page.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(Credential.email)
        login_page.find_element(LoginPageLocators.EMAIL_PASSWORD).send_keys(Credential.password)
        login_page.find_element(LoginPageLocators.ENTER_BUTTON).click()

        main_page.find_element(MainPageLocators.ACCOUNT_BUTTON).click()
        profile_page.find_element(ProfilePageLocators.HISTORY_BUTTON).click()
        account_orders_list = order_history_page.get_orders()  # Получаем список заказов из раздела «История заказов»
        main_page.find_element(MainPageLocators.ORDER_FEED_BUTTON).click()
        feed_page.check_orders(account_orders_list)  # Проверяем отображение заказов пользователя в «Ленте заказов»

    @allure.title('Проверка что при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_increase_counters(
            self,
            main_page: MainPage,
            login_page: LoginPage,
            feed_page: FeedPage,
            profile_page: ProfilePage
    ):
        # Авторизуемся
        main_page.find_element(MainPageLocators.ACCOUNT_BUTTON).click()
        login_page.find_element(LoginPageLocators.EMAIL_INPUT).send_keys(Credential.email)
        login_page.find_element(LoginPageLocators.EMAIL_PASSWORD).send_keys(Credential.password)
        login_page.find_element(LoginPageLocators.ENTER_BUTTON).click()

        # Переходим на «Лента заказов»
        main_page.find_element(MainPageLocators.ORDER_FEED_BUTTON).click()
        assert Urls.FEED_URL == profile_page.get_current_url()
        total_orders = feed_page.find_element(FeedPageLocators.TOTAL_ORDERS).text  # Заказов за все время
        today_orders = feed_page.find_element(FeedPageLocators.TODAY_ORDERS).text  # Заказов за сегодня

        # Переходим в «Конструктор»
        main_page.find_element(MainPageLocators.CONSTRUCTOR_BUTTON).click()
        main_page.drag_and_drop(MainPageLocators.INGREDIENTS, MainPageLocators.BURGER_CONSTRUCTOR)
        main_page.find_element(MainPageLocators.CREATE_ORDER_BUTTON).click()
        order_number = main_page.find_element(MainPageLocators.ORDER_NUMBER).text  # Номер заказа
        main_page.find_element(MainPageLocators.CLOSE_MODAL_BUTTON).click()
        main_page.find_element(MainPageLocators.ORDER_FEED_BUTTON).click()
        total_orders_after = feed_page.find_element(FeedPageLocators.TOTAL_ORDERS).text  # Заказов за все время
        assert int(total_orders_after) == int(total_orders) + 1

        # при создании нового заказа счётчик Выполнено за сегодня увеличивается
        today_orders_after = feed_page.find_element(FeedPageLocators.TODAY_ORDERS).text  # Заказов за сегодня
        assert int(today_orders_after) == int(today_orders) + 1

        # после оформления заказа его номер появляется в разделе В работе
        in_work_order_number = feed_page.find_element(FeedPageLocators.IN_WORK_ORDER_NUMBER).text
        assert order_number in in_work_order_number
