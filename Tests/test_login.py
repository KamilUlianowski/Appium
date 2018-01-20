from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_find_elements(driver):
    login = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "pl.com.bitcraft.siemapp:id/fragment_login_login_met"))
    )
    login.send_keys("kamilos")
    driver.hide_keyboard()
    password = driver.find_element_by_id("pl.com.bitcraft.siemapp:id/fragment_login_password_met")
    password.send_keys("qwerty")
    driver.hide_keyboard()
    submit = driver.find_element_by_id("pl.com.bitcraft.siemapp:id/fragment_login_login_btn")
    submit.click()