from Modules.Activities.base_activity import BaseActivity
from Modules.Helpers.custom_webdriver_functions import wait_for_element_and_click
from Modules.Locators.PhotoLab.device_gallery_locators import DeviceGalleryLocators
from Modules.Locators.PhotoLab.main_activity_locators import MainActivityLocators


class DeviceGallery(BaseActivity):
    def select_monkey(self):
        self.driver.wait_for_element_and_click(DeviceGalleryLocators.MENU_BTN)
        self.driver.wait_for_element_and_click(DeviceGalleryLocators.DOWNLOAD_BTN)
        self.driver.wait_for_element_and_click(DeviceGalleryLocators.MONKEY_IMAGE)