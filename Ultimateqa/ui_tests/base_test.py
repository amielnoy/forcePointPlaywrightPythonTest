import pytest
from Ultimateqa.pages.SubPages.sub_page_buttons import SubPageButtons
from Ultimateqa.pages.SubPages.sub_page_social_media import SubPageSocialMedia
from Ultimateqa.pages.SubPages.sub_page_forms import SubPageForms

class BaseTest:
    @pytest.fixture(autouse=True)
    def setup(self, page, base_url_fe):
        self.page = page
        self.base_url_fe = base_url_fe
        self.sub_page_buttons = SubPageButtons(self.page)
        self.sub_page_social_media = SubPageSocialMedia(self.page)
        self.sub_page_forms = SubPageForms(self.page)
        self.page.goto(self.base_url_fe)