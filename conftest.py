import pytest

@pytest.fixture
def webdriver(request):
    from selenium import webdriver
    driver = webdriver.Firefox()
    request.addfinalizer(driver.quit)
    return driver



