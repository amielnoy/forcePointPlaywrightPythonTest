# Sub_Page_button.py
from pickle import FALSE

import playwright
from playwright.sync_api import Page,expect


class SubPageButtons:
    def __init__(self, page: Page):
        self.page = page
        self.some_element = self.page.locator("#subpage1_element")

    def locate_button(self, index: int):
        return self.page.locator('.et_pb_button_'f'{index}')

    def does_button_exist(self, index: int) -> bool:
        current_button=self.locate_button(index)

        if current_button.is_visible():
          return True
        else:
          return False

    def count_buttons(self):
        count = 0
        while self.does_button_exist(count):
            count += 1
            print(count)
        return count

    def interact_with_element(self):
        self.some_element.click()

    def get_element_text(self):
        return self.some_element.text_content()
