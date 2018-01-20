from selenium.webdriver.common.by import By


class EditorActivityLocators(object):
    FIRST_EFFECT = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                              ".FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget"
                              ".HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout["
                              "1]/android.widget.FrameLayout/android.widget.ImageView[3]")

    PROGRESS_BAR = (By.ID, "com.jazzyworlds.photoeffectshattering:id/dotProgressBar1")
    SAVE_BTN = (By.ID, "com.jazzyworlds.photoeffectshattering:id/save_btn")
    SAVED_TEXT_TITLE = (By.ID, "com.jazzyworlds.photoeffectshattering:id/title")