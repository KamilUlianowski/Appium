import os
import pytest
from appium import webdriver

from Modules.Helpers.webdriver_extension import WebDriverExt


def pytest_addoption(parser):
   parser.addoption("--driver", action="store", default="chrome", help="Type in browser type")
   parser.addoption("--url", action="store", default="https://qa.moodle.net/", help="url")
   parser.addoption("--username", action="store", default="manager", help="username")
   parser.addoption("--password", action="store", default="test", help="password")


@pytest.fixture(autouse=True)
def driver():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    desired_caps['deviceName'] = "Nexus_5X_API_27_x86"
    # desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'siemApp_1.2.10.apk'))
    desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'spotify.apk'))
    selenium_driver = WebDriverExt('http://localhost:4723/wd/hub', desired_caps)
    # selenium_driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    yield selenium_driver

    selenium_driver.quit()

