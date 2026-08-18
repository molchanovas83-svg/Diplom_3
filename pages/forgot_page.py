from pages.base_page import BasePage
from locators.forgot_page_locators import ForgotPageLocators


class ForgotPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = ForgotPageLocators()



