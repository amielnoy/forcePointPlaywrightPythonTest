import sys
import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

class TestBase:
    @pytest.fixture(scope="function")
    def setup(self,page: Page):
        # Add the project path to sys.path
        load_dotenv()
        self.page = page
        self.base_url = os.getenv("BASE_URL")
        # Load environment variables

        # Retrieve the base URL from environment variables
        
        # Teardown code