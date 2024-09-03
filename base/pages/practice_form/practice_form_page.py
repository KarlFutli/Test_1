from playwright.sync_api import Page

from base.page_factory.button import Button
from base.page_factory.input import Input


class PracticeFormPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        """Локаторы страницы: Форма"""
        self.first_name = Input(page, locator='//*[@id="firstName"]', name='Имя')
        self.last_name = Input(page, locator='//*[@id="lastName"]', name='Фамилия')
        self.email = Input(page, locator='//*[@id="userEmail"]', email='Почта')
        self.gender = Button(page, locator='//*[@id="gender-radio-1"]', name='Пол')
        self.drop_month = page.locator('//*[starts-with(@class, "react-datepicker__month")]')
        self

        """Ожидания"""
        self.Wait_first_name = '//*[@id="firstName"]'
        self.Wait_last_name = '//*[@id="lastName"]'
        self.wait_email = '//*[@id="userEmail"]'
        self.Wait_drop_month = '(//*[starts-with(@class, "react-datepicker__month")])[2]'

        """Текст"""
        self.Name_text = 'Иван'