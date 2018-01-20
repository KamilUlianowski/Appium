
import os
import unittest

import time
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class ChessAndroidTests(unittest.TestCase):
    "Class to run tests against the Chess Free app"

    def setUp(self):
        "Setup for the test"
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '8.1'
        desired_caps['deviceName'] = 'Nexus 5X'
        # desired_caps["noReset"] = "true"
        # Returns abs path relative to this file and not cwd
        desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'app-offline-debug (2).apk'))
        # desired_caps['appPackage'] = "pl.com,bitcraft.siemapp"
        # desired_caps['appPackage'] = 'uk.co.aifactory.chessfree'
        # desired_caps['appActivity'] = 'pl.com.bitcraft.flow.activities.MainActivity'
        # desired_caps['appWaitActivity'] = 'pl.com.bitcraft.flow.activities.StartActivity'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def tearDown(self):
        "Tear down the test"
        self.driver.quit()


    def test_single_player_mode(self):
        # Click on Ignore update button
        element = WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located((By.ID, "android:id/button2"))
        )
        self.driver.find_element_by_id("android:id/button2").click()

        # Click on no button
        # element = WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_element_located((By.ID, "android:id/button2"))
        # )
        # self.driver.find_element_by_id("android:id/button2").click()

        # Move the screen to the left
        #
        # window_size = self.driver.get_window_size()
        #
        # self.driver.swipe(window_size['width'] * 0.9, window_size['height'] * 0.8, window_size['width'] * 0.1,
        #                   window_size['height'] * 0.8)
        element = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(By.ID, "io.loot.lootapp.offline:id/activity_intro_login_btn")
        )

        self.driver.find_element_by_id("io.loot.lootapp.offline:id/activity_intro_login_btn").click()

        # Click on log in button
        # element = WebDriverWait(self.driver, 15).until(
        #     EC.element_to_be_clickable((By.CLASS_NAME, "io.loot.lootapp.offline:id/activity_intro_login_btn"))
        # )
        # self.driver.find_element_by_id("io.loot.lootapp.offline:id/activity_intro_login_btn").click()
        #
        # # Click on not now button (screenshots)
        # element = WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_element_located((By.ID, "io.loot.lootapp.offline:id/fragment_protect_your_data_allow_btn"))
        # )
        # self.driver.find_element_by_id("io.loot.lootapp.offline:id/fragment_protect_your_data_allow_btn").click()
        #
        # # Click on not now button (screenshots)
        # element = WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_element_located((By.ID, "com.android.packageinstaller:id/permission_allow_button"))
        # )
        # self.driver.find_element_by_id("com.android.packageinstaller:id/permission_allow_button").click()
        #
        # # Enter email
        # element = WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_element_located((By.ID, "io.loot.lootapp.offline:id/fragment_login_email_met"))
        # )
        # self.driver.find_element_by_id("io.loot.lootapp.offline:id/fragment_login_email_met").send_keys("android@test.looot.io")
        #
        # # Enter password
        # element = WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_element_located((By.ID, "io.loot.lootapp.offline:id/fragment_login_password_met"))
        # )
        # self.driver.find_element_by_id("io.loot.lootapp.offline:id/fragment_login_password_met").send_keys("Password1")
        #
        # # Click on log in button
        # element = WebDriverWait(self.driver, 15).until(
        #     EC.presence_of_element_located((By.ID, "io.loot.lootapp.offline:id/fragment_login_login_pbbtn"))
        # )
        # self.driver.find_element_by_id("io.loot.lootapp.offline:id/fragment_login_login_pbbtn").click()

# ---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(ChessAndroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)