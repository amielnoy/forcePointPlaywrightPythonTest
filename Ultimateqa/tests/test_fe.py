import sys
import os
import pytest
from playwright.async_api import expect

from Ultimateqa.tests.base_test import TestBase
from playwright.sync_api import Page
from Ultimateqa.pages.SubPages.sub_page_buttons import SubPageButtons


sys.path.append('/Users/amielpeled/PycharmProjects/ForcePoint/Ultimateqa')


class TestsSuite(TestBase):
   
    def test_count_buttons(self,setup):
        expected_buttons_number=12
        # Initialize the sub-page object
        self.page.goto(self.base_url)
        sub_page_buttons = SubPageButtons(self.page)
        # Verify content section
        total_button_number=sub_page_buttons.count_buttons()
        assert sub_page_buttons.count_buttons() == expected_buttons_number
        print(f"Total count of Buttons=: {total_button_number}=={expected_buttons_number}")


    def test_facebook_follow_urls(self,page: Page):
        # Locate all elements with the title "Follow on Facebook"
        facebook_follow_elements = page.locator('[title="Follow on Facebook"]')
        # Expected URL for the "Follow on Facebook" link
        expected_url = "https://www.facebook.com/Ultimateqa1/"
        # Assert that each element has the expected URL
        for i in range(facebook_follow_elements.count()):
            element = facebook_follow_elements.nth(i)
            href = element.get_attribute("href")
            expect(href).to_have_url(expected_url)

        print(f"All 'Follow on Facebook' elements have the expected URL: {expected_url}")
