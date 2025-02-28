# Sub_Page_button.py
from playwright.sync_api import Page

class SubPageSocialMedia:
    def __init__(self, page: Page):
        self.page = page
        self.some_element = self.page.locator("#subpage1_element")

    def interact_with_element(self):
        self.some_element.click()

    def get_element_text(self):
        return self.some_element.text_content()
