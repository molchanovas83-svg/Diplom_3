from selenium.webdriver.common.by import By


class ProfilePageLocators:
    HISTORY_BUTTON = By.XPATH, "//*[contains(@href, '/account/order-history')]"
    EXIT_BUTTON = By.XPATH, "//*[contains(@type, 'button') and contains(., 'Выход')]"


