import pytest

from Pages.LoginPage import LoginPage


@pytest.fixture()
def abrir_browser():
    login_page = LoginPage()
    yield login_page
    login_page.close()

