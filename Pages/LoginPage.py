import selenium
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


class LoginPage():

    UserName_TXT = (By.ID,'loginIas_UserName')#Define Username field
    #text_area.send_keys('Administrator')#Enter Username

    Password_TXT = (By.ID,'loginIas_Password')#Define Password field
    #text_area.send_keys('P@ssw0rd')#Enter Password

    Submit_BTN = (By.ID,'loginIas_LoginButton')#Define Login Button

    Invalid_Data_TXT =(By.ID,'loginIas_FailureText')
    Username_Required_TXT =(By.ID,'loginIas_UserNameRequired')
    Password_Required_TXT =(By.ID,'loginIas_PasswordRequired')


  #Method to check that login is successful
    def login(self,username,password):
        self.driver.find_element(*LoginPage.UserName_TXT).send_keys(username)
        self.driver.find_element(*LoginPage.Password_TXT).send_keys(password)
        self.driver.find_element(*LoginPage.Submit_BTN).click()

    #Method to clear credentails
    def clear_Credentials(self):
        self.driver.find_element(*LoginPage.UserName_TXT).clear()
        self.driver.find_element(*LoginPage.Password_TXT).clear()

    #Method to check the invalid login
    def Invalid_login(self):
        Label_TXT = self.driver.find_element(*LoginPage.Invalid_Data_TXT).text
        return Label_TXT

    #Method to check that username is required
    def Username_required(self):
        Label_TXT = self.driver.find_element(*LoginPage.Username_Required_TXT).text
        return Label_TXT
    #Method to check that password is required
    def Password_required(self):
        Label_TXT = self.driver.find_element(*LoginPage.Password_Required_TXT).text
        return Label_TXT