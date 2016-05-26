import selenium
import select
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

class DG_Details():
    ReturnToDG_btn= (By.CSS_SELECTOR,'#ctl00_ctl00_MasterPageContent_cpv_lbReturnToList')
    def returnDG(self):
        self.driver.find_element(*DG_Details.ReturnToDG_btn).click()

    AssignDS_btn=(By.CSS_SELECTOR,'buttonUpdateDS')
    def AssignDS(self):
        self.driver.find_element(*DG_Details.AssignDS_btn).click()

    AssignPmps_btn=(By.CSS_SELECTOR,'#lbEditDG')
    def Assignpmp(self):
        self.driver.find_element(*DG_Details.AssignPmps_btn).click()

    UnAssignPmp_btn=(By.CSS_SELECTOR,'#ctl00_ctl00_MasterPageContent_cpv_lbUnAssignPumps')
    def UnAssignpmp(self):
        self.driver.find_element(*DG_Details.UnAssignPmp_btn).click()

#Screen appearance assertion
    def screen_displayed(self,how,what):
     try: self.driver.find_element(by=how,value=what)
     except NoSuchElementException as e:return False
     return True

