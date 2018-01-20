from selenium.webdriver.common.by import By

class DeviceGalleryLocators(object):
    MONKEY_IMAGE = (By.XPATH, "//android.widget.TextView[contains(@text, 'monkey')]")
    MENU_BTN = (By.XPATH, '//android.widget.ImageButton[@content-desc="Show roots"]')

    DOWNLOAD_BTN = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                              ".FrameLayout/android.view.ViewGroup/android.support.v4.widget.DrawerLayout/android"
                              ".widget.LinearLayout["
                              "2]/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout["
                              "3]/android.widget.FrameLayout[1]")