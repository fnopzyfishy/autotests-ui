import pytest
from playwright.sync_api import expect, Page


@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("user", [
    {"email": "user.name@gmail.com", "password": "password"},
    {"email": "user.name@gmail.com", "password": "  "},
    {"email": "  ", "password": "password"},
])
def test_wrong_email_or_password_authorization(chromium_page: Page, user):  # Создаем тестовую функцию
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.get_by_test_id('login-form-email-input').locator('input')
    email_input.fill(user["email"])

    password_input = chromium_page.get_by_test_id('login-form-password-input').locator('input')
    password_input.fill(user["password"])

    login_button = chromium_page.get_by_test_id('login-page-login-button')
    login_button.click()

    wrong_email_or_password_alert = chromium_page.get_by_test_id('login-page-wrong-email-or-password-alert')
    expect(wrong_email_or_password_alert).to_be_visible()
    expect(wrong_email_or_password_alert).to_have_text("Wrong email or password")