import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage():

    UserName_TXT = (By.ID,'loginIas_UserName')#Define Username field
    #text_area.send_keys('Administrator')#Enter Username

    Password_TXT = (By.ID,'loginIas_Password')#Define Password field
    #text_area.send_keys('P@ssw0rd')#Enter Password

    Submit_BTN = (By.ID,'loginIas_LoginButton')#Define Login Button

    def login(self,username,password):
        self.driver.find_element(*LoginPage.UserName_TXT).send_keys(username)
        self.driver.find_element(*LoginPage.Password_TXT).send_keys(password)
        self.driver.find_element(*LoginPage.Submit_BTN).click()

