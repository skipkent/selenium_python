from base_page import BasePage
from selenium.webdriver.common.by import By

class PythonOrgPage(BasePage):

    search_input = (By.NAME, "q")
    submit_button = (By.CSS_SELECTOR, "button#submit")

    def search_for_text(self, text):
        self.input_text_to_element(self.search_input, text)
        self.click(self.submit_button) 

    def do_something_with_the_inherited_driver(self):
        self.driver.find_element(*self.search_input)  # not needed, just demonstrating

