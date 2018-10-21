from pages.mabl_page import MablPage

mabl_url = "https://app.mabl.com/login"

def test_login(webdriver, test_user, test_password):
    webdriver.get(mabl_url)
    page = MablPage(webdriver)
    page.login_as(test_user, test_password)
    assert "Explore mabl" in page.get_page_source()

def test_navbar(webdriver, test_user, test_password):
    webdriver.get(mabl_url)
    page = MablPage(webdriver)
    page.login_as(test_user, test_password)
    assert "Explore mabl" in page.get_page_source()
    page.click(page.nav_plans)
    assert "A plan defines where and when mabl will test your app's functionality" in page.get_page_source()
