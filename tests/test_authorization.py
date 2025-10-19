import pytest
from playwright.sync_api import expect, Page

from pages.login_page import LoginPage


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("user", [
    {"email": "user.name@gmail.com", "password": "password"},
    {"email": "user.name@gmail.com", "password": "  "},
    {"email": "  ", "password": "password"},
])
def test_wrong_email_or_password_authorization(login_page: LoginPage, user):  # Создаем тестовую функцию
    login_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    login_page.fill_login_form(email=user["email"], password=user["password"])
    login_page.click_login_button()

    login_page.check_visible_wrong_email_or_password_alert()