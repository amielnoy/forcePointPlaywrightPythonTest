import os
from dotenv import load_dotenv
import pytest
from api_tests.api_client import APIClient

@pytest.fixture(scope="session")
def api():
    return APIClient()


@pytest.fixture(scope='session',autouse=True)
def base_url_fe():
    load_dotenv()
    return  os.getenv('BASE_URL_FE')

@pytest.fixture(scope='session',autouse=True)
def base_url_api():
    load_dotenv()
    APIClient.BASE_URL_API = os.getenv('BASE_URL_API')