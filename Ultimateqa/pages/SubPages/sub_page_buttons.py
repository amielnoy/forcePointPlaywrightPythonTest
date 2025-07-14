from playwright.sync_api import Page


class SubPageButtons:
    def __init__(self, page: Page):
        self.page = page
        self.some_element = self.page.locator("#subpage1_element")
        self.all_buttons= self.page.locator("[class^='et_pb_button_']")

    def locate_button(self, index: int):
        return self.page.locator(f'.et_pb_button_{index}')

    def does_button_exist(self, index: int) -> bool:
        current_button = self.locate_button(index)

        if current_button.is_visible():
            return True
        else:
            return False

    def count_buttons(self):
        count = 0
        while self.does_button_exist(count):
            count += 1
        return count
    def count_buttons_by_class(self):
        return self.all_buttons.count()

