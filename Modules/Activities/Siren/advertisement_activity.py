from Modules.Activities.base_activity import BaseActivity
from Modules.Helpers.custom_webdriver_functions import wait_for_element_and_click
from Modules.Locators.Siren.advertisement_activity_locators import AdvertisementActivityLocators
from Modules.Locators.Siren.main_activity_locators import MainActivityLocators
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AdvertisementActivity(BaseActivity):
    def close_adds(self):
        try:
            # wait_for_element_and_click(self.driver, AdvertisementActivityLocators.CLOSE_BTN, 3)
            self.driver.wait_for_element_and_click(AdvertisementActivityLocators.CLOSE_BTN, 3)
        except:
            return