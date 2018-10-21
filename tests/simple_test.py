from pages.python_org_page import PythonOrgPage

def test_the_search(webdriver):
    webdriver.get("http://www.python.org")
    assert "Python" in webdriver.title
    python_org_page = PythonOrgPage(webdriver)
    python_org_page.search_for_text("pycon")
    assert "No results found." not in python_org_page.get_page_source()

def test_the_search_again(webdriver):
    webdriver.get("http://www.python.org")
    assert "Wildebeest" not in webdriver.title
    python_org_page = PythonOrgPage(webdriver)
    python_org_page.search_for_text("pycon")
    assert "PyCon Argentina" in python_org_page.get_page_source()
