import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config, browser

from utils import attach


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.window_height = 1920
    browser.config.window_width = 1080


@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browsers = Browser(Config(driver))
    yield browsers

    attach.add_screenshot(browsers)
    attach.add_logs(browsers)
    attach.add_html(browsers)
    attach.add_video(browsers)

    browsers.quit()
