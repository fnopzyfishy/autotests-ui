from playwright.sync_api import Page, expect

from components.base_component import BaseComponent


class ChartViewComponent(BaseComponent):
    def __init__(self, page: Page, identifier, chart_type):
        super().__init__(page)

        self.title = page.get_by_test_id(f'{identifier}-widget-title-text')
        self.title_text = identifier.capitalize()
        self.chart_type = page.get_by_test_id(f'{identifier}-{chart_type}-chart')

    def check_visible(self):
        expect(self.title).to_be_visible()
        expect(self.title).to_have_text(self.title_text)
        expect(self.chart_type).to_be_visible()