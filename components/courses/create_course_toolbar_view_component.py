import allure
from playwright.sync_api import Page

from components.base_component import BaseComponent
from elements.button import Button
from elements.text import Text


class CreateCourseToolbarViewComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.title = Text(page, 'courses-list-toolbar-title-text', 'Title')
        self.create_course_button = Button(page, 'courses-list-toolbar-create-course-button', 'Create Course')

    @allure.step('Check visible create course toolbar element and check button status')
    def check_visible(self, is_created_course_disabled: bool = True):
        self.title.check_visible()

        if is_created_course_disabled:
            self.create_course_button.check_disabled()

        if not is_created_course_disabled:
            self.create_course_button.check_enabled()

    def click_create_course_button(self):
        self.create_course_button.click()