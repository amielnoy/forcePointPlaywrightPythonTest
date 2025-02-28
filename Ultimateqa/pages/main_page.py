from playwright.sync_api import Page

from SubPages.sub_page_buttons import SubPageButtons
from SubPages.sub_page_social_media import SubPageSocialMedia
from SubPages.sub_page_forms import SubPageForms


class MainPage:
    def __init__(self, page: Page):
        super().__init__(page)
        self.sub_page_buttons = SubPageButtons(page)
        self.sub_page_social_media = SubPageSocialMedia(page)
        self.sub_page_forms = SubPageForms(page)

# Usage in a test
