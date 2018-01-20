import os
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Modules.Activities.Siren.advertisement_activity import AdvertisementActivity
from Modules.Activities.Siren.main_activity import MainActivity
from Modules.Activities.Siren.songs_activity import SongsActivity
from Modules.Helpers.webdriver_extension import WebDriverExt


def test_play_song():

    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '8.1.0'
    desired_caps['deviceName'] = "Nexus_5X_API_27_x86"
    desired_caps['app'] = os.path.abspath(os.path.join(os.path.dirname(__file__), 'siren_horen.apk'))


    selenium_driver = WebDriverExt('http://localhost:4723/wd/hub', desired_caps)
    main_activity = MainActivity(selenium_driver)
    adds_activity = AdvertisementActivity(selenium_driver)
    songs_activity = SongsActivity(selenium_driver)
    main_activity.go_to_songs()
    adds_activity.close_adds()
    songs_activity.play_song()
    songs_activity.check_if_the_music_is_played()
    assert (songs_activity.check_if_the_music_is_played() == True)
    selenium_driver.quit()

