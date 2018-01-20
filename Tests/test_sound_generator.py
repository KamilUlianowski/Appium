import os
import time

from appium.webdriver.common.touch_action import TouchAction

from Modules.Helpers.webdriver_extension import WebDriverExt


def test_play_song():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    desired_caps['deviceName'] = "Nexus_5X_API_27_x86"
    desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'generator_dzwieku.apk'))
    selenium_driver = WebDriverExt('http://localhost:4723/wd/hub', desired_caps)

    play_btn = selenium_driver.find_element_by_id("com.boedec.hoel.frequencygenerator:id/playButton")
    seekbar = selenium_driver.find_element_by_id("com.boedec.hoel.frequencygenerator:id/seekbar")

    x = seekbar.location['x']
    y = seekbar.location['y']
    width = seekbar.size['width']
    action = TouchAction(selenium_driver)
    play_btn.click()
    action.press(None, 0.5*x, 0.5*y).move_to(None, 0.1*width, y).release().perform()
    action.press(None, 0.1*width, y).move_to(None, 0.3*width, y).release().perform()
    action.press(None, 0.3*width, y).move_to(None, 0.5*width, y).release().perform()
    action.long_press(None, 0.5*width, y).move_to(None, 0.7*width, y).release().perform()
    action.long_press(None, 0.7*width, y).move_to(None, 0.5*width, y).release().perform()
    action.long_press(None, 0.5*width, y).move_to(None, 0.9*width, y).release().perform()
    action.long_press(None, 0.9*width, y).move_to(None, width, y).release().perform()

    frequency = selenium_driver.find_element_by_id("com.boedec.hoel.frequencygenerator:id/editFreq").text

    assert (frequency, '22000')

    time.sleep(10)
    selenium_driver.quit()

