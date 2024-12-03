from playwright.sync_api import Page
from sub_page_buttons import SubPageButtons
from sub_page_social_media import SubPageSocialMedia
from sub_page_forms import SubPageForms


class MainPage:
    def _init_(self, page: Page):
        self.page = page
        self.sub_page_buttons = SubPageButtons(page)
        self.sub_page_social_media = SubPageSocialMedia(page)
        self.sub_page_forms = SubPageForms(page)

# Usage in a test
