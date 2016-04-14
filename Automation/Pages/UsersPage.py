import selenium
from selenium.webdriver.common.by import By

class UsersPage():
    Users_BTN = (By.LINK_TEXT,'Users')
    Create_BTN= (By.LINK_TEXT,'Create')


    def Users(self):
        self.driver.find_element(*UsersPage.Users_BTN).click()
        self.driver.find_element(*UsersPage.Create_BTN).click()


class Add_Users():
    First_name_LBL=(By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtFirstName')
    Last_name_LBL=(By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtLastName')
    User_name_LBL=(By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtEmployeeId')
    Password_LBL=(By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtPassword')
    Retype_Password_LBL=(By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtRetypePassword')
    Save_Create_BTN=(By.CSS_SELECTOR,'body > div:nth-child(4) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span')

    def Multi_Users(self,first_name,last_name,user_name,password,re_password):
        self.driver.find_element(*Add_Users.First_name_LBL).send_keys(first_name)
        self.driver.find_element(*Add_Users.Last_name_LBL).send_keys(last_name)
        self.driver.find_element(*Add_Users.User_name_LBL).send_keys(user_name)
        self.driver.find_element(*Add_Users.Password_LBL).send_keys(password)
        self.driver.find_element(*Add_Users.Retype_Password_LBL).send_keys(re_password)
        self.driver.find_element(*Add_Users.Save_Create_BTN).click()


