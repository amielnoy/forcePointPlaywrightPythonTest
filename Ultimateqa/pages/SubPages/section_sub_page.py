import sys
import os
from dotenv import load_dotenv
from playwright.sync_api import Page
from sub_page_buttons import SubPageButtons

class SectionSubPage:
    def __init__(self,page: Page):
        self.page=page
        self.name_element =self.page.locator('#et_pb_contact_name_0')
        self.email_element = self.page.locator('#et_pb_contact_email_0')
        self.message_element = self.page.locator('#et_pb_contact_message_0')
        self.contact_submit_button= self.page.locator('.et_pb_contact_submit')

    def fill_contact_form(self, name: str, email: str, message: str):
        # Fill the contact form fields
        self.name_element.fill(name)
        self.email_element.fill(email)
        self.message_element.fill(message)

    def submit_contact_form(self):
        # Submit the contact form
        self.contact_submit_button.click()