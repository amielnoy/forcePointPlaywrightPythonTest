import sys
import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from sub_page_buttons import SubPageButtons

class SectionSubPage:
    def setup(self, page: Page, goto):
        # Add the project path to sys.path
        sys.path.append('/')

        # Load environment variables
        load_dotenv()

        # Retrieve the base URL from environment variables
        base_url = os.getenv("BASE_URL")

        # Navigate to the base URL
        goto(base_url)

        # Initialize the sub-page buttons object
        self.sub_page_buttons = SubPageButtons(page)

    def fill_contact_form(self, name: str, email: str, message: str):
        # Fill the contact form fields
        self.page.fill('#et_pb_contact_name_0', name)
        self.page.fill('#et_pb_contact_email_0', email)
        self.page.fill('#et_pb_contact_message_0', message)

    def submit_contact_form(self):
        # Submit the contact form
        self.page.click('.et_pb_contact_submit')