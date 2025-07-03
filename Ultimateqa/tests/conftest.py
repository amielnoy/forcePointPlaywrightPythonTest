import os
import pytest
from dotenv import load_dotenv
from playwright.sync_api import Page

# @pytest.fixture
# def goto(page: Page):
#     def _goto(url: str):
#         page.goto(url)
#     return _goto

@pytest.fixture(scope='session',autouse=True)
def base_url():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    dotenv_path = os.path.join(project_root, '.env')
    load_dotenv(dotenv_path=dotenv_path)
    base_url=os.getenv('BASE_URL')
    return base_url
