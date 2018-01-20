import time
from appium.webdriver.common.touch_action import TouchAction

from Modules.Activities.base_activity import BaseActivity
from Modules.Locators.Siren.main_activity_locators import MainActivityLocators
from Modules.Locators.Siren.songs_activity_locators import SongsActivityLocators

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SongsActivity(BaseActivity):
    def play_song(self):
        window_size = self.driver.get_window_size()
        finded = False

        while(finded == False):
            self.driver.swipe(window_size['width'] * 0.3, window_size['height'] * 0.65, window_size['width'] * 0.3,
                              window_size['height'] * 0.15)
            try:
                second_song = self.driver.find_element(*SongsActivityLocators.SONG_TO_PLAY)
                finded = True
            except:
                pass
        if second_song is not None:
            second_song.click()


    def check_if_the_music_is_played(self):
        try:
            self.driver.find_element(*SongsActivityLocators.PAUSE_BTN)
            return True
        except:
            return False
