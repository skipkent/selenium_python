from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from python_org_page import PythonOrgPage

driver = webdriver.Firefox()

def setup_module(module):
    driver.get("http://www.python.org")

def test_the_search():
    assert "Python" in driver.title
    python_org_page = PythonOrgPage(driver)
    python_org_page.search_for("pycon")
    assert "No results found." not in python_org_page.get_page_source()

def test_the_search_again():
    assert "Python" in driver.title
    python_org_page = PythonOrgPage(driver)
    python_org_page.search_for("pycon")
    assert "PyCon Argentina" in python_org_page.get_page_source()

def teardown_module(module):
    driver.quit()