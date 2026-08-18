from selenium.webdriver.common.by import By


class OrderHistoryPageLocators:
    ORDERS = By.XPATH, "//*[contains(@class, 'OrderHistory_textBox')]//*[contains(@class, 'text_type_digits-default')]"
