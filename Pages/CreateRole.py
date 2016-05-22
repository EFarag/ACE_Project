import selenium
from selenium.webdriver.common.by import By

# roles
class RolesPage():
    Roles_BTN = (By.LINK_TEXT,'Roles')

    def Roles (self):
      self.driver.find_element(*RolesPage.Roles_BTN).click()

class Create():
    Create_BTN = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_labelCreate')

    def btn_Create(self):
        self.driver.find_element(*Create.Create_BTN).click()


class Role_Creation():
    Role_Name = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtRoleName')
    Role_Option = (By.CSS_SELECTOR,'html.firefox-45 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable div#DivCreateRole.popup.ui-dialog-content.ui-widget-content div div.inline-Block div.inline-Block div.bloc select#ctl00_ctl00_MasterPageContent_cpv_lstboxAllPermissions.inner-container option')
    MoveLeft_BTN = (By.ID,'MoveLeft')
    Save_BTN = (By.XPATH,'/html/body/div[3]/div[3]/div/button[1]')


    def Role(self,name):
        self.driver.find_element(*Role_Creation.Role_Name).send_keys(name)
        self.driver.find_element(*Role_Creation.Role_Option).click()
        self.driver.find_element(*Role_Creation.MoveLeft_BTN).click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(*Role_Creation.Save_BTN).click()




class Create_Role_MSG():
    Msg_Label = (By.XPATH,'/html/body/div[4]/div[2]')
    def Role_Message(self):
     self.driver.implicitly_wait(5)
     Msg_TXT = self.driver.find_element(*Create_Role_MSG.Msg_Label).text
     return Msg_TXT