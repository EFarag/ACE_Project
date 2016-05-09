import selenium
import select
from selenium.webdriver.common.by import By

class DG_Create():
    CreateDG_btn = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_lbCreate')
    def DG_create(self):
        self.driver.find_element (*DG_Create.DG_btn).click()

class DG_edit():
    Edit_btn=(By.XPATH,'/html/body/form/div[8]/section/section/div[1]/div[1]/a[2]')
    def DG_edit(self):
        self.driver.find_element (*DG_edit.Edit_btn).click

class DG_delete():
    Delete_btn=(By.XPATH,'/html/body/form/div[8]/section/section/div[1]/div[1]/a[3]')
    def  DG_delete(self):
        self.driver.find_element (*DG_delete.Delete_btn).click


class DG_DetailsPopup():
    DG_Name = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_dialogTxtDeploymentGroupName')
    DG_Description=(By.ID,'ctl00_ctl00_MasterPageContent_cpv_dialogTxtAreaDeploymentGroupDescription')
    DG_DB=(By.XPATH,'/html/body/div[3]/div[2]/table/tbody/tr[7]/td[2]/')
    DG_SaveConBtn=(By.XPATH,'/html/body/div[3]/div[3]/div/button[1]')
    DG_SaveCloseBtn=(By.XPATH,'/html/body/div[3]/div[3]/div/button[2]')
    DG_CancelBtn=(By.XPATH,'/html/body/div[3]/div[3]/div/button[3]')
    def DG_DetailsPopup(self):
        self.driver.find_element(*DG_DetailsPopup.DG_Name).send_keys('Group1')
        self.driver.find_element(*DG_DetailsPopup.DG_Description).send_keys('Group1')
        self.driver.find_element(*DG_DetailsPopup.DG_SaveConBtn).click()
        self.driver.find_element(*DG_DetailsPopup.DG_SaveCloseBtn).click()
        self.driver.find_element(*DG_DetailsPopup.DG_CancelBtn).click()
        self.driver.find_elemeny(*DG_DetailsPopup.DG_DB).select_by_value('(local)\AGWII\CQI')
