from Modules.Activities.base_activity import BaseActivity
from Modules.Helpers.custom_webdriver_functions import wait_for_element_and_click
from Modules.Locators.PhotoLab.main_activity_locators import MainActivityLocators


class MainActivity(BaseActivity):
    def close_adds(self):
        try:
            self.driver.wait_for_element_and_click(MainActivityLocators.CLOSE_ADDS_BTN, 3)
        except:
            pass

    def go_to_gallery(self):
        self.driver.wait_for_element_and_click(MainActivityLocators.DEVICE_GALLERY_BTN)

    def go_to_art_effect(self):
        self.driver.wait_for_element_and_click(MainActivityLocators.ART_EFFECT_BTN)

    def go_to_shattering_effect(self):
        self.driver.wait_for_element_and_click(MainActivityLocators.SHATTERING_EFFECT_BTN)
