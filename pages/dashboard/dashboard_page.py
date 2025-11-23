from playwright.sync_api import Page

from components.charts.chart_view_component import ChartViewComponent
from components.dashboard.dashboard_toolbar_view_component import DashboardToolbarViewComponent
from components.navigation.navbar_component import NavbarComponent
from components.navigation.sidebar_component import SidebarComponent
from pages.base_page import BasePage


class DashboardPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.navbar = NavbarComponent(page)
        self.sidebar = SidebarComponent(page)
        self.student_bar_chart = ChartViewComponent(page, 'students', 'bar')
        self.activities_line_chart = ChartViewComponent(page, 'activities', 'line')
        self.courses_pie_chart = ChartViewComponent(page, 'courses', 'pie')
        self.scores_scatter_chart = ChartViewComponent(page, 'scores', 'scatter')
        self.dashboard_toolbar = DashboardToolbarViewComponent(page)
    
    def check_visible_scores_chart(self):
        self.scores_scatter_chart.check_visible("Scores")

    def check_visible_courses_chart(self):
        self.courses_pie_chart.check_visible("Courses")

    def check_visible_students_chart(self):
        self.student_bar_chart.check_visible("Students")

    def check_visible_activities_chart(self):
        self.activities_line_chart.check_visible("Activities")