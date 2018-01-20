import time
from selenium.webdriver.support.wait import WebDriverWait

from Modules.Activities.base_activity import BaseActivity
from Modules.Helpers.custom_webdriver_functions import wait_for_element_and_click
from Modules.Locators.PhotoLab.editor_activity_locators import EditorActivityLocators
from Modules.Locators.PhotoLab.main_activity_locators import MainActivityLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class EditorActivity(BaseActivity):
    def choose_first_effect(self):
        self.driver.wait_for_element_and_click(EditorActivityLocators.FIRST_EFFECT)

    def save_image(self):

        self.driver.wait_for_element_and_click(EditorActivityLocators.SAVE_BTN)

    def check_if_saved(self):
        try:
            self.driver.wait_for_element(EditorActivityLocators.SAVED_TEXT_TITLE, 3)
            return True
        except:
            return False

    def wait_for_end_progressbar(self):
        self.driver.wait_for_element_until_invisible(EditorActivityLocators.PROGRESS_BAR)

    def wait_for_progressbar(self):
        self.driver.wait_for_element(EditorActivityLocators.PROGRESS_BAR)