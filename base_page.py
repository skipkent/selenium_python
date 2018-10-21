from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
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
        print "waiting for visible..."
        self.wait_for_element_visible(by)
        print "getting element..."
        elem = self.driver.find_element(*by)
        print "clicking..."
        elem.click()

    def wait_for_element_visible(self, by):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(by))

    def sleep(self, seconds):
        time.sleep(seconds)