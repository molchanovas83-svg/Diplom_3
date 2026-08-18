import allure
from pages.base_page import BasePage
from locators.order_history_page_locators import OrderHistoryPageLocators


class OrderHistoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = OrderHistoryPageLocators()

    @allure.step('Получаем список заказов из раздела «История заказов»')
    def get_orders(self):
        account_orders = self.find_elements(self.locators.ORDERS)
        account_orders_numbers = [order.text for order in account_orders]
        return account_orders_numbers
