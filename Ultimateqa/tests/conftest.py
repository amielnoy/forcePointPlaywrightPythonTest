import pytest
from playwright.sync_api import Page

@pytest.fixture
def goto(page: Page):
    def _goto(url: str):
        page.goto(url)
    return _goto