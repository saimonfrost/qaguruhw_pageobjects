import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    browser.config.timeout = 3

    yield

    browser.quit()
