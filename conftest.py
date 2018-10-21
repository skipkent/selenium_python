import pytest
import os

@pytest.fixture
def webdriver(request):
    from selenium import webdriver
    driver = webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return driver

@pytest.fixture
def test_user():
    return os.environ["TEST_USERNAME"]

@pytest.fixture
def test_password():
    return os.environ["TEST_PASSWORD"]


