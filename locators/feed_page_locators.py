from selenium.webdriver.common.by import By


class FeedPageLocators:
    ORDER = By.XPATH, "//*[contains(@class, 'OrderHistory_listItem')]"
    ORDER_NUMBER = By.XPATH, ("//*[contains(@class, 'OrderHistory_textBox')]"
                              "//*[contains(@class, 'text_type_digits-default')]")
    IN_WORK_ORDER_NUMBER = By.XPATH, ("(//*[contains(@class, 'OrderFeed_orderList__')])[2]"
                                      "//*[contains(@class, 'text_type_digits-default')]")
    ORDER_FEED_MODAL = By.XPATH, ("//*[contains(@class, 'Modal_modal_opened')]"
                                  "//*[contains(@class, 'Modal_modal__container')]")
    CLOSE_FEED_MODAL_BUTTON = By.XPATH, ("//*[contains(@class, 'Modal_modal_opened')]"
                                         "//button[contains(@class, 'Modal_modal__close_modified')]")
    TOTAL_ORDERS = By.XPATH, "(//*[contains(@class, 'OrderFeed_number')])[1]"
    TODAY_ORDERS = By.XPATH, "(//*[contains(@class, 'OrderFeed_number')])[2]"
