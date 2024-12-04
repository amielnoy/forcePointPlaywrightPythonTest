from dotenv import load_dotenv
import os

from playwright.sync_api import Page
from Ultimateqa.pages.sub_page_buttons import SubPageButtons


def test_count_buttons(page: Page, goto):
    sub_page_buttons = SubPageButtons(page)
    load_dotenv()
    base_url = os.getenv("BASE_URL")
    goto(base_url)

    # Interact with header section
    # main_page.header.navigate_to_about()

    # Verify content section
    assert sub_page_buttons.count_buttons() == 12
