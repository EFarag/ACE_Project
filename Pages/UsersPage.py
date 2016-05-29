import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

class Users():

    Users_BTN = (By.LINK_TEXT,'Users')
    Create_BTN= (By.LINK_TEXT,'Create')

    def Users_Link(self):
        self.driver.find_element(*Users.Users_BTN).click()
    def Create_Link(self):
        self.driver.find_element(*Users.Create_BTN).click()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
    First_name_LBL=(By.ID, 'ctl00_ctl00_MasterPageContent_cpv_txtFirstName')
    Last_name_LBL=(By.ID, 'ctl00_ctl00_MasterPageContent_cpv_txtLastName')
    Title_LBL = (By.ID, 'ctl00_ctl00_MasterPageContent_cpv_drpTitle')
    Role_LBL = (By.ID, 'ctl00_ctl00_MasterPageContent_cpv_drpRole')
    User_name_LBL=(By.ID, 'ctl00_ctl00_MasterPageContent_cpv_txtEmployeeId')
    Password_LBL=(By.ID, 'ctl00_ctl00_MasterPageContent_cpv_txtPassword')
    Retype_Password_LBL=(By.ID, 'ctl00_ctl00_MasterPageContent_cpv_txtRetypePassword')
    Language_LBL = (By.ID, 'ctl00_ctl00_MasterPageContent_cpv_drpLanguage')
    Save_Create_BTN=(By.CSS_SELECTOR, 'body > div:nth-child(4) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1) > span')


    def CreateUsers(self,first_name,last_name,title, role,user_name,password,re_password, language):
        self.driver.find_element(*Users.First_name_LBL).send_keys(first_name)
        sleep(2)
        self.driver.find_element(*Users.Last_name_LBL).send_keys(last_name)
        sleep(2)
        Select(self.driver.find_element(*Users.Title_LBL)).select_by_visible_text(title)
        sleep(2)
        Select(self.driver.find_element(*Users.Role_LBL)).select_by_visible_text(role)
        sleep(2)
        self.driver.find_element(*Users.User_name_LBL).send_keys(user_name)
        sleep(2)
        self.driver.find_element(*Users.Password_LBL).send_keys(password)
        sleep(2)
        self.driver.find_element(*Users.Retype_Password_LBL).send_keys(re_password)
        sleep(2)
        Select (self.driver.find_element(*Users.Language_LBL)).select_by_visible_text(language)
        sleep(2)
        self.driver.find_element(*Users.Save_Create_BTN).click()
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    Creation_PopUp_LBL = (By.ID, 'ui-id-3')
    def PopUpAssertion_LBL (self):
        Label_TXT = self.driver.find_element(*Users.Creation_PopUp_LBL).text
        return Label_TXT

    Creation_PopUp_Body= (By.ID, 'divConfirm')
    def PopUpAssertion_Body (self):
        Body_TXT = self.driver.find_element(*Users.Creation_PopUp_Body).text
        return Body_TXT

    Popup_Btn = (By.XPATH, 'html/body/div[4]/div[3]/div')
    def OK (self):
        self.driver.find_element(*Users.Popup_Btn).click()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

    def Select_User (self, first_name):
        User_Checkbox = (By.XPATH, "//span[contains(text(), '" + str(first_name)  + "')]/preceding-sibling::span/img")
        (self.driver.find_element(*User_Checkbox)).click()

    Delete_User = (By.ID , 'ctl00_ctl00_MasterPageContent_cpv_lbDelete')
    Confirm_Delete = (By.XPATH, 'html/body/div[3]/div[3]/div/button[1]')
    def Remove_User (self):
        self.driver.find_element(*Users.Delete_User).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*Users.Confirm_Delete).click()





