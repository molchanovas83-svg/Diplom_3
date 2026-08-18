from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL_INPUT = By.XPATH, "//*[contains(@type, 'text')]"
    EMAIL_PASSWORD = By.XPATH, "//*[contains(@type, 'password')]"
    ENTER_BUTTON = By.XPATH, "//button[contains(@class, 'button_button_type_primary') and contains(., 'Войти')]"
    FORGOT_PASSWORD_BUTTON = By.XPATH, "//*[contains(@class, 'Auth_link') and contains(text(), 'Восстановить пароль')]"
    FORGOT_PASSWORD_EDIT = By.XPATH, "//input[contains(@class, 'text input__textfield')]"
