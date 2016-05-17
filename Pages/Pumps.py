import selenium
import select

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select

from ddt import ddt,data,unpack
import unittest

class Pumps():
    Pumps_Page= (By.CSS_SELECTOR,'html.firefox-46 body form#aspnetForm div#wrapper div.home-wrap div.sections div.home-section div#ctl00_MasterPageContent_rptHomeMenu_ctl02_ctl00_ctl01_div_itemSection.item-section div.item-Wrap a#ctl00_MasterPageContent_rptHomeMenu_ctl02_ctl00_ctl01_MenuLink.subsection')
    def Pumps_link (self):
        self.driver.find_element(*Pumps.Pumps_Page).click()

    Import_btn = (By.ID, 'ctl00_ctl00_MasterPageContent_cpv_lbImportPump')
    def Import_Pump (self):
        self.driver.find_element(*Pumps.Import_btn).click()

    Browse_btn= (By.ID, 'ctl00_ctl00_MasterPageContent_cpv_ctlFileUpload')
    Continue_btn = (By.XPATH, '/html/body/div[5]/div[3]/div/button[1]')
    def Browse_File (self, Location):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*Pumps.Browse_btn).send_keys(Location)
        self.driver.find_element(*Pumps.Continue_btn).click()

    OK_btn = (By.ID, 'ui-button ui-widget ui-state-default ui-corner-all ui-button-text-only')
    def Ok_Import (self):
        self.driver.find_element(*Pumps.OK_btn).click()

    Cancel_btn = (By.XPATH, 'html/body/div[5]/div[3]/div/button[2]')
    def Cancel_Import (self):
        self.driver.find_element(*Pumps.Cancel_btn).click()

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Popup_Assertion():
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
         print('Test Failed') #TimeoutError







