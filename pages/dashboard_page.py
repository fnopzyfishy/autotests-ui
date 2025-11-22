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
