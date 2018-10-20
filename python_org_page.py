from selenium.webdriver.common.keys import Keys
import time

class PythonOrgPage():

    def __init__(self, driver):
        self.driver = driver

    def search_for(self, text):
        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys(text)
        elem.send_keys(Keys.RETURN)
        time.sleep(2)

    def get_page_source(self):
        return self.driver.page_source
