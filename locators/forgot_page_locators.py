from selenium.webdriver.common.by import By


class ForgotPageLocators:
    EMAIL_INPUT = By.XPATH, "//input[contains(@class, 'text input__textfield')]"
    RECOVERY_BUTTON = By.XPATH, ("//button[contains(@class, 'button_button_type_primary') "
                                 "and contains(., 'Восстановить')]")
    PASSWORD_ICON = By.XPATH, "//*[contains(@class, 'input__icon-action')]"
    PASSWORD_ACTIVE = By.XPATH, "//*[contains(@class, 'input_status_active')]"
