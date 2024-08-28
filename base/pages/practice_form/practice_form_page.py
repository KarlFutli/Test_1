from playwright.sync_api import Page


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Форма"""
        self.first_name = input(page, locator='//*[@id="firstName"]', name='Имя')
        self.last_name = input(page, locator='//*[@id="lastName"]', name='Фамилия')

        """Ожидание"""
        self.Wait_first_name = '//*[@id="firstName"]'
        self.Wait_last_name = '//*[@id="lastName"]'