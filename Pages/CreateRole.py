import selenium
from selenium.webdriver.common.by import By

# roles
class RolesPage():
    #Roles Page Locators
    Roles_BTN = (By.LINK_TEXT,'Roles')
    Create_BTN = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_labelCreate')
    Role_Name = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtRoleName')
    Role_Option = (By.CSS_SELECTOR,'html.firefox-45 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable div#DivCreateRole.popup.ui-dialog-content.ui-widget-content div div.inline-Block div.inline-Block div.bloc select#ctl00_ctl00_MasterPageContent_cpv_lstboxAllPermissions.inner-container option')
    MoveLeft_BTN = (By.ID,'MoveLeft')
    Save_BTN = (By.XPATH,'/html/body/div[3]/div[3]/div/button[1]')
    Msg_Label = (By.XPATH,'/html/body/div[4]/div[2]')

    #Method to click on Roles link on Home page
    def Roles (self):
      self.driver.find_element(*RolesPage.Roles_BTN).click()

    #Method to click on Create Role button
    def btn_Create(self):
        self.driver.find_element(*RolesPage.Create_BTN).click()

    #Method to create Role
    def Role(self,name):
        self.driver.find_element(*RolesPage.Role_Name).send_keys(name)
        self.driver.find_element(*RolesPage.Role_Option).click()
        self.driver.find_element(*RolesPage.MoveLeft_BTN).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*RolesPage.Save_BTN).click()

    #Method to check the confirmation message after creation
    def Role_Message(self):
     self.driver.implicitly_wait(5)
     Msg_TXT = self.driver.find_element(*RolesPage.Msg_Label).text
     return Msg_TXT