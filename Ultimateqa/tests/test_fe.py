import os
from playwright.sync_api import Page
from Ultimateqa.pages.main_page import MainPage

def test_count_buttons(page: Page, goto):
    main_page = MainPage(page)
    base_url = os.environ["BASE_URL"]
    goto(base_url)

    # Interact with header section
    main_page.header.navigate_to_about()

    # Verify content section
    assert main_page.sub_page_buttons.count_buttons() == 12
