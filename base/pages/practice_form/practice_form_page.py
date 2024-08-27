from playwright.sync_api import Page


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.first_name = self.page.locator()