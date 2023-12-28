import configparser
from selenium import webdriver
from selenium.webdriver.common.by import By

config = configparser.RawConfigParser()

config.read('/Users/utsav.jha/PycharmProjects/SlingApp/Locators/element.ini')


class signInApp:
    def __init__(self, driver):
        self.driver = driver

    def ClickProdEve(self):
        prod = config.get("Locator", "prod_env_X")
        self.driver.find_element_by_xpath(prod).click()

    def clickSignin(self):
        signinButton = config.get("Locator", "SignIn_button_x")
        self.driver.find_element_by_xpath(signinButton).click()

    def enterEmailPass(self,username,password):
        email = config.get("Locator", "Email_Box_x")
        pas = config.get("Locator", "Password_box_x")
        self.driver.find_element_by_xpath(email).send_keys(username)
        self.driver.find_element_by_xpath(pas).send_keys(password)

    def signInSubmit(self):
        submit = config.get("Locator", "SignIn_Submit_x")
        self.driver.find_element_by_xpath(submit).click()

    def profileTitle(self):
        title = config.get("Locator", "profileDashboardTitle_x")
        tit=self.driver.find_element_by_xpath(title)
        return tit.text
