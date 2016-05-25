import selenium
from selenium.webdriver.common.by import By
import time

# roles
class RolesPage():
    #Roles Page Locators
    Roles_BTN = (By.LINK_TEXT,'Roles')
    Create_BTN = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_labelCreate')
    Role_Name = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtRoleName')
    MoveLeft_BTN = (By.ID,'MoveLeft')
    Save_BTN = (By.XPATH,'/html/body/div[3]/div[3]/div/button[1]')
    Msg_Label = (By.XPATH,'/html/body/div[4]/div[2]')
    Options = (By.TAG_NAME,'option')
    Role_name_message =(By.ID,'ctl00_ctl00_MasterPageContent_cpv_labelRoleNameRequired')
    Edit_Move_Left_BTN = (By.ID,'btnUpdateMoveLeft')
    Edit_Move_Right_BTN =(By.ID,'btnUpdateMoveRight')
    Edit_Role_BTN =(By.ID,'ctl00_ctl00_MasterPageContent_cpv_rptRoles_ctl03_btnEditRole')
    Collapse_icon =(By.CSS_SELECTOR,'html.firefox-46 body form#aspnetForm div#wrapper section#main-content section.content-body table.multi-view tbody tr td.full-View div#ctl00_ctl00_MasterPageContent_cpv_UpdatePanel1 div#divscroll div.container h2.acc_trigger table tbody tr td span#ctl00_ctl00_MasterPageContent_cpv_rptRoles_ctl04_imgArrow.collapse-icon-right.imgArrow')
    Roles_Options = (By.XPATH, ".//*[@id='divscroll']/div/h2")
    Edit_Save =(By.XPATH,'html/body/div[3]/div[3]/div/button[1]')
    Update_Msg = (By.XPATH,".//*[@id='divConfirmChange']")
    Delete_Role =(By.ID,'ctl00_ctl00_MasterPageContent_cpv_labelDelete')
    Delete_Confirmation_popup = (By.CSS_SELECTOR,'.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only.ui-state-focus')
    Delete_Confirmation_Msg =(By.CSS_SELECTOR,'#divConfirmChange')

    #Method to click on Roles link on Home page
    def Roles(self):
      self.driver.find_element(*RolesPage.Roles_BTN).click()

    #Method to click on Create Role button
    def btn_Create(self):
        self.driver.find_element(*RolesPage.Create_BTN).click()

    def Select_Permissions(self,permission):
        options_List =[]
        options_List = self.driver.find_elements(*RolesPage.Options)
        for option in options_List:
         if option.text == permission:
          option.click() # select() in earlier versions of webdriver
          #break



    #Method to create Role
    def Role_name_Creation(self,name):
        self.driver.find_element(*RolesPage.Role_Name).send_keys(name)


    def Move_Left(self):
        self.driver.find_element(*RolesPage.MoveLeft_BTN).click()
        self.driver.implicitly_wait(10)

    def Save_Role(self):
        self.driver.find_element(*RolesPage.Save_BTN).click()

    #Method to check the confirmation message after creation
    def Role_Message(self):
     self.driver.implicitly_wait(5)
     Msg_TXT = self.driver.find_element(*RolesPage.Msg_Label).text
     return Msg_TXT



    def Role_name_missing(self):
     UpdateMsg_label = self.driver.find_element(*RolesPage.RUpdate_Msg).text
     return UpdateMsg_label





#******************************************Edit Functions******************************

    def Role_Edit(self, Role_name,Role_perm):
     Roles_List = []
     counter=1
     Roles_List = self.driver.find_elements(*RolesPage.Roles_Options)
     for option in Roles_List:
        roleLabel = option.find_element(By.XPATH, ".//table/tbody//tr/td[1]/span[1]")
        if roleLabel.text == Role_name:
            if(counter <= 9):
                self.arrowELem = self.driver.find_element(By.ID,"ctl00_ctl00_MasterPageContent_cpv_rptRoles_ctl0"+str(counter)+ "_imgArrow")
                self.editButton = self.driver.find_element(By.ID, "ctl00_ctl00_MasterPageContent_cpv_rptRoles_ctl0" + str(counter) + "_btnEditRole")
            else:
                self.arrowELem = self.driver.find_element(By.ID,"ctl00_ctl00_MasterPageContent_cpv_rptRoles_ctl"+str(counter)+ "_imgArrow")
                self.editButton = self.driver.find_element(By.ID, "ctl00_ctl00_MasterPageContent_cpv_rptRoles_ctl" + str(counter) + "_btnEditRole")

            self.arrowELem.click()
            time.sleep(2)
            self.editButton.click()

            rolePermissions = self.driver.find_elements(By.XPATH, ".//*[@id='ctl00_ctl00_MasterPageContent_cpv_lstboxUodateSelectedPermissions']/option")
            availablePermissions = self.driver.find_elements(By.XPATH, ".//*[@id='ctl00_ctl00_MasterPageContent_cpv_lstboxUpdateAllPermissions']/option")

            for list in availablePermissions:
                if list.text == Role_perm:
                    list.click()
                    time.sleep(2)
                    self.driver.find_element(*RolesPage.Edit_Move_Left_BTN).click()
                    time.sleep(3)
                    self.driver.find_element(*RolesPage.Edit_Save).click()
                    break

        counter += 1

       #Method to check the confirmation message after creation
    def UpdateRole_Message(self):
     self.driver.implicitly_wait(5)
     Msg_TXT = self.driver.find_element(*RolesPage.Msg_Label).text
     return Msg_TXT


        #**************************************Delete Role**************************



    def Role_Delete(self, DRole_name):
     Roles_List = []
     counter=1
     Roles_List = self.driver.find_elements(*RolesPage.Roles_Options)
     for option in Roles_List:
        roleLabel = option.find_element(By.XPATH, ".//table/tbody//tr/td[1]/span[1]")
        if roleLabel.text == DRole_name:
            if(counter <= 9):
                self.arrowELem = self.driver.find_element(By.ID,"ctl00_ctl00_MasterPageContent_cpv_rptRoles_ctl0"+str(counter)+ "_imgArrow")
            else:
                self.arrowELem = self.driver.find_element(By.ID,"ctl00_ctl00_MasterPageContent_cpv_rptRoles_ctl"+str(counter)+ "_imgArrow")


            self.arrowELem.click()
            time.sleep(2)
            self.driver.find_element(*RolesPage.Delete_Role).click()
            time.sleep(3)
            self.driver.find_element(*RolesPage.Delete_Confirmation_popup).click()

        counter += 1


    def DeleteRole_Message(self):
     self.driver.implicitly_wait(5)
     Msg_TXT = self.driver.find_element(*RolesPage.Delete_Confirmation_Msg).text
     return Msg_TXT
