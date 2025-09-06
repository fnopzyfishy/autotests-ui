"""
Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration
Заполнить форму регистрации и нажать на кнопку "Registration"
Сохранить состояние браузера
Создать новую сессию браузера. В контекст необходимо подставить сохраненное состояние
Открыть страницу https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses. Страница "Courses" должна открыться без авторизации
Проверить наличие и текст заголовка "Courses"
Проверить наличие и текст блока "There is no results"
Проверить наличие и видимость иконки пустого блока
Проверить наличие и текст описания блока: "Results from the load test pipeline will be displayed here"
"""

from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.fill('user@gmail.com')

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.fill('password')

    registration_button = page.get_by_test_id('registration-page-registration-button')
    registration_button.click()

    context.storage_state(path='browser-state.json')


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state='browser-state.json')
    page = context.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    course_title = page.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_title).to_have_text('Courses')

    no_result_title = page.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_result_title).to_have_text('There is no results')

    empty_list_icon = page.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_list_icon).to_be_visible()

    empty_description_text = page.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_description_text).to_have_text('Results from the load test pipeline will be displayed here')