import unittest
from DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.LoginPage import LoginPage
from Pages.Pumps import Pumps
from Pages.Pumps import Popup_Assertion
from time import sleep
from selenium.webdriver.common.by import By
import select

#----------------------------------------------- Cancel Import ----------------------------------------------------------------------------------------------------------------------
@ddt
class test_CancelPumpsImport(BaseTestCase):

    def test_Cancel(self):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        Pumps.Pumps_link(self)
        sleep(3)
        Pumps.Import_Pump(self)
        sleep(3)
        self.assertTrue(Popup_Assertion.is_element_present(self,how=By.CSS_SELECTOR, what='html.firefox-46 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable div.ui-dialog-titlebar.ui-widget-header.ui-corner-all.ui-helper-clearfix span#ui-id-2.ui-dialog-title'))
        Pumps.Cancel_Import(self)
        sleep(5)
        #self.assertTrue(Popup_Assertion.is_element_disabled(self,how=By.CSS_SELECTOR, what='html.firefox-46 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable div.ui-dialog-titlebar.ui-widget-header.ui-corner-all.ui-helper-clearfix span#ui-id-2.ui-dialog-title'))


@ddt#----------------------------------- Successful Pump Importing ------------------------------------------------------------------------
class test_PumpsImport(BaseTestCase):


    @data(*read_excel.get_data_from_excel('D:\Automation Python\ACE_Project\Data\login_data.xlsx','Pumps'))
    @unpack
    def test_Import(self,url):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        Pumps.Pumps_link(self)
        sleep(3)
        Pumps.Import_Pump(self)
        sleep(3)
        Pumps.Browse_File(self,url)
        sleep(5)
        self.assertTrue(Popup_Assertion.is_element_present(self,how=By.ID, what='ui-dialog ui-widget ui-widget-content ui-corner-all ui-front ui-dialog-buttons ui-draggable'))
        Pumps.Ok_Import(self)
        sleep(10)

@ddt #------------------------------ Negative Scenario Pump Importing ------------------------------------------------------------------------
class test_InvalidPumpsImport(BaseTestCase):


    @data(*read_excel.get_data_from_excel('D:\Automation Python\ACE_Project\Data\login_data.xlsx','Pumps'))
    @unpack
    def test_FailedImport(self, url):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        Pumps.Pumps_link(self)
        sleep(3)
        Pumps.Import_Pump(self)
        sleep(3)
        Pumps.Browse_File(self,url)
        sleep(5)
        #self.assertTrue(Popup_Assertion.is_element_present(self,how=By.ID, what='divImportPumpStatus'))
        Pumps.Ok_Import(self)
        sleep(10)



if __name__ == '__main__':
    unittest.main()
