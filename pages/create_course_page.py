from playwright.sync_api import Page, expect

from components.courses.create_course_exercise_form_component import CreateCourseExerciseFormComponent
from components.courses.create_course_exercises_toolbar_view_component import CreateCourseExercisesToolbarViewComponent
from components.courses.create_course_form_component import CreateCourseFormComponent
from components.courses.create_course_toolbar_view_component import CreateCourseToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.views.empty_view_component import EmptyViewComponent
from components.views.image_upload_widget_component import ImageUploadWidgetComponent
from elements.button import Button
from elements.text import Text
from pages.base_page import BasePage


class CreateCoursePage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.image_upload_widget = ImageUploadWidgetComponent(page, 'create-course-preview')
        self.exercises_empty_view = EmptyViewComponent(page, 'create-course-exercises')
        self.create_exercise_form = CreateCourseExerciseFormComponent(page)
        self.navbar = NavbarComponent(page)
        self.create_course_form = CreateCourseFormComponent(page)
        self.create_course_toolbar = CreateCourseToolbarViewComponent(page)
        self.create_course_exercises_toolbar = CreateCourseExercisesToolbarViewComponent(page)

        self.create_course_title = Text(page, 'create-course-toolbar-title-text', 'Create course')
        self.create_course_button = Button(page, 'create-course-toolbar-title-text', 'Create course button')

    def check_visible_create_course_title(self):
        self.create_course_title.check_visible()
        self.create_course_title.check_have_text('Create course')

    def click_create_course_button(self):
        self.create_course_button.click()

    def check_visible_create_course_button(self):
        self.create_course_button.check_visible()

    def check_disabled_create_course_button(self):
        self.create_course_button.check_disabled()

    def check_visible_exercises_empty_view(self):
        self.exercises_empty_view.check_visible(
            title='There is no exercises',
            description='Click on "Create exercise" button to create new exercise'
        )
