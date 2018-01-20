from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class WebDriverExt(WebDriver):
    def __init__(self, url, desired_caps):
        super().__init__(url, desired_caps)


    def wait_for_element_and_click(self, element, time=15):
        WebDriverWait(self, time).until(
            EC.element_to_be_clickable(element)
        )
        self.find_element(*element).click()

    def wait_for_element_and_send_text(self, element, text, time=15):
        WebDriverWait(self, time).until(
            EC.presence_of_element_located(element)
        )
        self.find_element(*element).clear()
        self.find_element(*element).send_keys(text)
        self.hide_keyboard()


    def check_if_element_is_visible(self, element, time=15):
        try:
            WebDriverWait(self, time).until(
                EC.presence_of_element_located(element)
            )
            return True
        except TimeoutException:
            return False

    def check_if_element_is_invisible(self, element, time=15):
        try:
            WebDriverWait(self, time).until(
                EC.invisibility_of_element_located(element)
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_and_get_text(self, element, time=15):
        WebDriverWait(self, time).until(
            EC.presence_of_element_located(element)
        )
        return self.find_element(*element).text

    def wait_for_element_and_get_text_from_input(self, element, time=15):
        WebDriverWait(self, time).until(
            EC.presence_of_element_located(element)
        )
        return self.find_element(*element).get_attribute("value")

    def wait_and_get_element(self, element, time=5):
        WebDriverWait(self, time).until(
            EC.presence_of_element_located(element)
        )
        return self.find_element(*element)

    def wait_for_element(self, element, time=5):
        WebDriverWait(self, time).until(
            EC.presence_of_element_located(element)
        )

    def wait_for_element_until_invisible(self, element, time=15):
        WebDriverWait(self, time).until(
            EC.invisibility_of_element_located(element)
        )