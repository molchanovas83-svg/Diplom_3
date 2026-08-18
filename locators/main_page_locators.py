from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = By.XPATH, "//*[contains(@class, 'AppHeader_header__linkText') and contains(., 'Конструктор')]"
    ORDER_FEED_BUTTON = By.XPATH, "//*[contains(@href, '/feed')]"
    ACCOUNT_BUTTON = By.XPATH, "//*[contains(@class, 'AppHeader_header') and contains(text(), 'Личный Кабинет')]"
    INGREDIENTS = By.XPATH, "//*[contains(@class, 'BurgerIngredient_ingredient') and contains(@draggable,'true')]"
    INGREDIENTS_MODAL = By.XPATH, ("//*[contains(@class, 'Modal_modal_opened')]"
                                   "//*[contains(@class, 'Modal_modal__container')]")
    CLOSE_MODAL_BUTTON = By.XPATH, ("//*[contains(@class, 'Modal_modal_opened')]"
                                    "//button[contains(@class, 'Modal_modal__close_modified')]")
    BURGER_CONSTRUCTOR = By.XPATH, "//*[contains(@class, 'BurgerConstructor_basket__list__')]"
    COUNTER_INGREDIENT = By.XPATH, "//*[contains(@class, 'counter_counter__num')]"
    ENTER_TO_ACCOUNT_BUTTON = By.XPATH, ("//button[contains(@class, 'button_button_type_primary') "
                                         "and contains(., 'Войти в аккаунт')]")
    CREATE_ORDER_BUTTON = By.XPATH, ("//button[contains(@class, 'button_button_type_primary') "
                                     "and contains(., 'Оформить заказ')]")
    ORDER_NUMBER = By.XPATH, ("//*[contains(@class, 'Modal_modal__contentBox')]"
                              "//*[contains(@class, 'text_type_digits-large')]")
