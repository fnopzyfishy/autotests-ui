import pytest
from playwright.sync_api import expect, Page

@pytest.mark.regression
@pytest.mark.courses
def test_empty_courses_list(chromium_page_with_state: Page):
    page = chromium_page_with_state
    chromium_page_with_state.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses'
    )

    course_title = chromium_page_with_state.get_by_test_id('courses-list-toolbar-title-text')
    expect(course_title).to_have_text('Courses')

    no_result_title = chromium_page_with_state.get_by_test_id('courses-list-empty-view-title-text')
    expect(no_result_title).to_have_text('There is no results')

    empty_list_icon = chromium_page_with_state.get_by_test_id('courses-list-empty-view-icon')
    expect(empty_list_icon).to_be_visible()

    empty_description_text = chromium_page_with_state.get_by_test_id('courses-list-empty-view-description-text')
    expect(empty_description_text).to_have_text('Results from the load test pipeline will be displayed here')