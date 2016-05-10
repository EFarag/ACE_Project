import selenium
import select
from selenium.webdriver.common.by import By
from time import sleep

class DG_Create():

    DG_screen= (By.CSS_SELECTOR,'html.firefox-42 body form#aspnetForm div#wrapper div.home-wrap div.sections div.home-section div#ctl00_MasterPageContent_rptHomeMenu_ctl01_ctl00_ctl02_div_itemSection.item-section div.item-Wrap a#ctl00_MasterPageContent_rptHomeMenu_ctl01_ctl00_ctl02_MenuLink.subsection')
    def DG_screenlink (self):
        self.driver.find_element(*DG_Create.DG_screen).click()
    CreateDG_btn = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_lbCreate')
    def DG_createlink (self):
        self.driver.find_element (*DG_Create.CreateDG_btn).click()

    Edit_btn=(By.XPATH,'/html/body/form/div[8]/section/section/div[1]/div[1]/a[2]')
    def DG_edit(self):
        self.driver.find_element (*DG_Create.Edit_btn).click()

    Delete_btn=(By.XPATH,'/html/body/form/div[8]/section/section/div[1]/div[1]/a[3]')
    def  DG_delete(self):
        self.driver.find_element (*DG_Create.Delete_btn).click()

    DG_Name = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_dialogTxtDeploymentGroupName')
    DG_Description=(By.ID,'ctl00_ctl00_MasterPageContent_cpv_dialogTxtAreaDeploymentGroupDescription')
    DG_DB=(By.ID,'ctl00_ctl00_MasterPageContent_cpv_cqiDatabaseDropDownList')
    DG_SaveConBtn=(By.XPATH,'/html/body/div[3]/div[3]/div/button[1]')
    DG_SaveCloseBtn=(By.XPATH,'/html/body/div[3]/div[3]/div/button[2]')
    DG_CancelBtn=(By.XPATH,'/html/body/div[3]/div[3]/div/button[3]')
    def DG_DetailsPopup(self):
        self.driver.find_element(*DG_Create.DG_Name).send_keys('Group1')
        sleep(3)
        self.driver.find_element(*DG_Create.DG_Description).send_keys('Group1')
        sleep(3)
        self.driver.find_element(*DG_Create.DG_SaveConBtn).click()
        sleep(3)
        self.driver.find_element(*DG_Create.DG_SaveCloseBtn).click()
        sleep(3)
        self.driver.find_element(*DG_Create.DG_CancelBtn).click()
        sleep(10)
        self.driver.find_element(*DG_Create.DG_DB).select_by_value('(local)\AGWII\CQI').click()
        sleep(10)
