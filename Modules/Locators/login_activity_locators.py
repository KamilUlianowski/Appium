from selenium.webdriver.common.by import By


class LoginActivityLocators(object):
    LOGIN_INPUT = (By.ID, "pl.com.bitcraft.siemapp:id/fragment_login_login_met")
    PASSWORD_INPUT = (By.ID, "pl.com.bitcraft.siemapp:id/fragment_login_password_met")
    LOGIN_BTN = (By.ID, "pl.com.bitcraft.siemapp:id/fragment_login_login_btn")
