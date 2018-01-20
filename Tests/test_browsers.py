import os

import time
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Modules.Activities.PhotoLab.device_gallery import DeviceGallery
from Modules.Activities.PhotoLab.editor_activity import EditorActivity
from Modules.Activities.PhotoLab.main_activity import MainActivity
from Modules.Helpers.webdriver_extension import WebDriverExt


def test_play_song():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    desired_caps['deviceName'] = "Nexus_5X_API_27_x86"
    desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'photolab.apk'))
    selenium_driver = WebDriverExt('http://localhost:4723/wd/hub', desired_caps)

    main_activity = MainActivity(selenium_driver)
    device_galery = DeviceGallery(selenium_driver)
    editor_activity = EditorActivity(selenium_driver)

    main_activity.go_to_shattering_effect()
    main_activity.go_to_gallery()
    device_galery.select_monkey()
    editor_activity.choose_first_effect()
    editor_activity.wait_for_progressbar()
    editor_activity.wait_for_end_progressbar()
    editor_activity.save_image()
    assert(editor_activity.check_if_saved() == True)


    selenium_driver.quit()

