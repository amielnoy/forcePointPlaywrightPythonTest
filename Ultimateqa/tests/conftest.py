import pytest


@pytest.fixture
def goto(self, url: str):
    self.page.goto(url)