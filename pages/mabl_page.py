from base_page import BasePage
from selenium.webdriver.common.by import By
import time

class MablPage(BasePage):

    login_with_google = (By.CSS_SELECTOR, ".onboarding-blue-button")
    kwood_online = (By.CSS_SELECTOR, "[data-email='kwood.online@gmail.com']")
    username_input = (By.CSS_SELECTOR, "input[type='email']")
    password_input = (By.CSS_SELECTOR, "input[type='password']")
    submit_button = (By.CSS_SELECTOR, "button[type='submit']")

    dashboard_title = (By.CSS_SELECTOR, ".page-content .fa-dashboard")

    # nav buttons
    nav_dashboard = (By.CSS_SELECTOR, "#side-menu .fa-dashboard")
    nav_plans = (By.CSS_SELECTOR, "#side-menu .fa-tasks")
    nav_configuration = (By.CSS_SELECTOR, "#side-menu .fa-cubes")
    nav_settings = (By.CSS_SELECTOR, "#side-menu .fa-cog")

    def login_as_kent(self):
        self.click(self.login_with_google)
        self.click(self.kwood_online) 

    def login_as(self, username, password):
        self.input_text_to_element(self.username_input, username)
        self.input_text_to_element(self.password_input, password)
        self.click(self.submit_button)
        self.wait_for_element_visible(self.dashboard_title)


    def do_something_with_the_inherited_driver(self):
        self.driver.find_element(*self.search_input)  # not needed, just demonstrating