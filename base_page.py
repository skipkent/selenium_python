from selenium.webdriver.common.keys import Keys
import time

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def get_page_source(self):
        return self.driver.page_source

    def input_text_to_element(self, by, text):
        elem = self.driver.find_element(*by)
        elem.clear()
        elem.send_keys(text)

    def click(self, by):
        elem = self.driver.find_element(*by)
        elem.click()

    def wait_for_element_visible(self, by):
        pass