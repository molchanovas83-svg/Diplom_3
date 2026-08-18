import allure
from pages.base_page import BasePage
from locators.feed_page_locators import FeedPageLocators


class FeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = FeedPageLocators()

    @allure.step('Проверяем что заказы из раздела «История заказов» отображаются на странице «Лента заказов»')
    def check_orders(self, account_orders):
        feed_orders = self.find_elements(self.locators.ORDER_NUMBER)
        feed_order_numbers = [order.text for order in feed_orders]
        assert all(item in feed_order_numbers for item in account_orders) is True
