import action as action
import selenium
import select
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

from ddt import ddt,data,unpack
import unittest
class DG_Create():
    DG_screen= (By.CSS_SELECTOR,'html.firefox-42 body form#aspnetForm div#wrapper div.home-wrap div.sections div.home-section div#ctl00_MasterPageContent_rptHomeMenu_ctl01_ctl00_ctl02_div_itemSection.item-section div.item-Wrap a#ctl00_MasterPageContent_rptHomeMenu_ctl01_ctl00_ctl02_MenuLink.subsection')
    def DG_screenlink (self):
        self.driver.find_element(*DG_Create.DG_screen).click()

#Deployment group screen buttons
    CreateDG_btn = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_lbCreate')
    def DG_createlink (self):
        self.driver.find_element (*DG_Create.CreateDG_btn).click()

    Edit_btn=(By.XPATH,'/html/body/form/div[8]/section/section/div[1]/div[1]/a[2]')
    def DG_edit(self):
        self.driver.find_element (*DG_Create.Edit_btn).click()

    Delete_btn=(By.CSS_SELECTOR,'#ctl00_ctl00_MasterPageContent_cpv_lbDelete')
    def DG_delete(self):
       self.driver.find_element(*DG_Create.Delete_btn).click()
       # self.driver.find_element(*DG_Create.Delete_btn).click()


    DG_Checkbox=(By.XPATH,'html/body/form/div[8]/section/section/div[2]/div[1]/div/table/tbody/tr[2]/td[1]/span[1]/img')
    def DG_CB(self):
        self.driver.find_element(*DG_Create.DG_Checkbox).click()
        self.driver.implicitly_wait(10)
#Create Deployment Group popup controls:
    DG_Name = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_dialogTxtDeploymentGroupName')
    DG_Description=(By.ID,'ctl00_ctl00_MasterPageContent_cpv_dialogTxtAreaDeploymentGroupDescription')
    DG_DB=(By.ID,'ctl00_ctl00_MasterPageContent_cpv_cqiDatabaseDropDownList')
    #DG_DB = (By.CSS_SELECTOR,'table tbody tr td select#ctl00_ctl00_MasterPageContent_cpv_cqiDatabaseDropDownList')
    DG_SaveConBtn=(By.XPATH,'/html/body/div[3]/div[3]/div/button[1]')
    DG_SaveCloseBtn=(By.XPATH,'/html/body/div[3]/div[3]/div/button[2]')
    DG_CancelBtn=(By.XPATH,'/html/body/div[3]/div[3]/div/button[3]')
    DG_toast=(By.CSS_SELECTOR,'html.firefox-42 body div.blockUI.toast.blockPage')
    Name_req=(By.CSS_SELECTOR,'#ctl00_ctl00_MasterPageContent_cpv_labelDeploymentGroupNameRequired')
    Desc_req=(By.CSS_SELECTOR,'#ctl00_ctl00_MasterPageContent_cpv_labelAreaDeploymentGroupDescriptionRequired')
    DB_req=(By.CSS_SELECTOR,'#ctl00_ctl00_MasterPageContent_cpv_cqiDatabaseSelectionRequired')

#DG popup functions
    def DG_DetailsPopup(self,name,desc,index):
        self.driver.find_element(*DG_Create.DG_Name).send_keys(name)
        sleep(3)
        self.driver.find_element(*DG_Create.DG_Description).send_keys(desc)
        DGDB_DDL = Select(self.driver.find_element(*DG_Create.DG_DB))
        print(len(DGDB_DDL.options))
        DGDB_DDL.select_by_index(index)
        sleep(3)
        self.driver.implicitly_wait(10)

    def save_close_btn(self):
        self.driver.find_element(*DG_Create.DG_SaveCloseBtn).click()
        self.driver.implicitly_wait(10)

    def save_cont_btn(self):
        self.driver.find_element(*DG_Create.DG_SaveConBtn).click()

    def Cancel(self):
        self.driver.find_element(*DG_Create.DG_CancelBtn).click()

    def ReqName(self):
        ReqName_error=self.driver.find_element(*DG_Create.Name_req).text
        return ReqName_error

    def ReqDesc(self):
        ReqDesc_error=self.driver.find_element(*DG_Create.Desc_req).text
        return  ReqDesc_error

    def ReqDB(self):
        ReqDB_error=self.driver.find_element(*DG_Create.DB_req).text
        return ReqDB_error

# DG Toast message
    def Toast(self):
        Label_TXT = self.driver.find_element(*DG_Create.DG_toast).text
        return Label_TXT

    #def DG_toast(self,DGname):
     #self.driver.implicitly_wait(5)
     #if self.driver.find_element(*DG_Create.DG_toast).text == "Deployment Group " + DGname + " has been created.":
      #   return True
     #print("Msh is " + Msg_TXT)
     #return Msg_TXT

#Create DG popup appearance assertion
    def is_element_present(self,how,what):
     try: self.driver.find_element(by=how,value=what)
     except NoSuchElementException as e:return False
     return True

    def is_element_disabled(self,how,what):
     try: self.driver.find_element(by=how,value=what)
     except NoSuchElementException as e:return True
     if True:
         return False

     else:
         print('Test Failed')


#Deployment Group Delete popup
    Delete_popup=(By.CSS_SELECTOR,'#popup-deleteDeploymentGroup')
    Delete_warning=(By.CSS_SELECTOR,'#ctl00_ctl00_MasterPageContent_cpv_labelDeleteWarning')
    Delete_con_btn=(By.CSS_SELECTOR,'.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only.ui-state-focus')
    Confirm_deletionPassword=(By.CSS_SELECTOR,'#ctl00_ctl00_MasterPageContent_cpv_tbPassword')
    Delete_btn=(By.CSS_SELECTOR,'.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only')

#This function is to return warning message before deployment group deletion inorder to assert it in the test case
    def warning_delete(self):
        Warning_text=self.driver.find_element(*DG_Create.Delete_warning).text
        return Warning_text
#This function is to click on continue deletion button
    def complete_delete(self):
        self.driver.find_element(*DG_Create.Delete_con_btn).click()
        self.driver.find_element(*DG_Create.Confirm_deletionPasswordPassword).send_keys("P@ssw0rd")
        self.driver.find_element(*DG_Create.Delete_btn).click()
#This function is to set login password to complete deletion and then click on delete button
