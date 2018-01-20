from selenium.webdriver.common.by import By

class SongsActivityLocators(object):
    ALARM_1 = (By.XPATH, "//android.widget.TextView[contains(@text, 'Alarm-1')]")
    ALARM_5 = (By.XPATH, "//android.widget.TextView[contains(@text, 'Alarm-5')]")
    SONG_TO_PLAY = (By.XPATH, "//android.widget.TextView[contains(@text, 'Rain Alarm')]")

    # SHIP_HORM = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
    #                        "2]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.LinearLayout"
    #                        "/android.widget.ListView/android.widget.RelativeLayout[6]/android.widget.TextView")

    SONG_TIME = (By.ID, "com.andromo.dev449458.app415575:id/time_current")
    PAUSE_BTN = (By.ID, "com.andromo.dev449458.app415575:id/pause")
