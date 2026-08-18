import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from seletools.actions import drag_and_drop


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        self.scrolling_to_element(element)
        return element

    def find_elements(self, locator):
        elements = WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))
        return elements

    def wait_for_clickable(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.scrolling_to_element(element)
        return element

    def wait_invisibility(self, locator):
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    def scrolling_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center', inline: 'center'});", element)
        time.sleep(1)

    def get_current_url(self):
        time.sleep(1)
        return self.driver.current_url

    def switch_to_window(self):
        new_window = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_window)
        time.sleep(1)

    def close_window(self):
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[0])

    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(*source_locator)
        target = self.driver.find_element(*target_locator)
        drag_and_drop(self.driver, source, target)
