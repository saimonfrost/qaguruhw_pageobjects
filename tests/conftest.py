import pytest
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from utils import attach


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        'selenoid:options': {
            'enableVNC': True,
            'enableVideo': True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_width = 2500
    browser.config.window_height = 2500
    browser.config.base_url = 'https://demoqa.com'
    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_video(browser)
    attach.add_logs(browser)

    browser.quit()
