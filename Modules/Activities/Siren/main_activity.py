from Modules.Activities.base_activity import BaseActivity
from Modules.Helpers.custom_webdriver_functions import wait_for_element_and_click
from Modules.Locators.Siren.main_activity_locators import MainActivityLocators


class MainActivity(BaseActivity):
    def go_to_songs(self):
        # wait_for_element_and_click(self.driver, MainActivityLocators.LOGIN_INPUT)
        self.driver.wait_for_element_and_click(MainActivityLocators.LOGIN_INPUT)