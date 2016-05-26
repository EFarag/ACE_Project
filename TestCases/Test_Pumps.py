import unittest

from selenium.webdriver.common.by import By
from BaseTestCases.BaseTestCase import BaseTestCase
from DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from Pages.LoginPage import LoginPage
from Pages.Pumps import Pumps
from Pages.Pumps import Popup_Assertion
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import os.path


@ddt
class test_Pumps(BaseTestCase):

#----------------------------------------------- Cancel Import ----------------------------------------------------------------------------------------------------------------------
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

#----------------------------------- Successful Pump Importing --------------------------------------------------------------------------------------------------------------------
    @data(*read_excel.get_data_from_excel(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +  '\\Data\\Test_Data.xlsx','Pumps'))
    @unpack
    def test_Import(self,url):
        File_location = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +'\\Data\\' + url
        print(File_location)
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        Pumps.Pumps_link(self)
        sleep(3)
        Pumps.Import_Pump(self)
        sleep(3)
        Pumps.Browse_File(self,File_location)
        sleep(2)
        Pumps.Continue_Import(self)
        sleep(3)
        self.assertTrue(Popup_Assertion.is_element_present(self,how=By.CSS_SELECTOR, what='.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable'))
#--------------------------------- Popup text assertion --------------------------------------------------------------------------------------------------------------
        Import_Popup = Pumps.Import_Toast(self)
        print(Import_Popup)
        self.assertEqual( Import_Popup,'Number of pumps imported:8\n\nNumber of pumps NOT imported:0')
        Pumps.Ok_Import(self)
        sleep(10)

#------------------------------ Negative Scenario Pump Importing -------------------------------------------------------------------------------------------------------------------------
    @data(*read_excel.get_data_from_excel(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +  '\\Data\\Test_Data.xlsx','Pumps'))
    @unpack
    def test_FailedImport(self, url):
        File_location = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +'\\Data\\' + url
        print(File_location)
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        Pumps.Pumps_link(self)
        sleep(3)
        Pumps.Import_Pump(self)
        sleep(3)
        Pumps.Browse_File(self,File_location)
        sleep(5)
        Pumps.Continue_Import(self)
        sleep(3)
        self.assertTrue(Popup_Assertion.is_element_present(self,how=By.ID, what='divImportPumpStatus'))
#--------------------------------- Popup text assertion --------------------------------------------------------------------------------------------------------------
        Import_Popup = Pumps.Import_Toast(self)
        print(Import_Popup)
        self.assertEqual( Import_Popup,'Number of pumps imported:0\n\nNumber of pumps NOT imported:2')
        Pumps.Ok_Import(self)
        sleep(10)
        Pumps.Ok_Import(self)
        sleep(10)

#------------------------------ Duplicate Scenario Pump Importing -----------------------------------------------------------------------------------------------------------------------------
    @data(*read_excel.get_data_from_excel(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +  '\\Data\\Test_Data.xlsx','Pumps'))
    @unpack
    def test_DuplicateImport(self,url):
        File_location = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +'\\Data\\' + url
        print(File_location)
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        Pumps.Pumps_link(self)
        sleep(3)
        Pumps.Import_Pump(self)
        sleep(3)
        Pumps.Browse_File(self,File_location)
        sleep(5)
        Pumps.Continue_Import(self)
        sleep(3)
        self.assertTrue(Popup_Assertion.is_element_present(self,how=By.CSS_SELECTOR, what='.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable'))
#--------------------------------- Popup text assertion --------------------------------------------------------------------------------------------------------------
        Import_Popup = Pumps.Import_Toast(self)
        print(Import_Popup)
        self.assertEqual( Import_Popup,'Number of pumps imported:0\n\nNumber of pumps NOT imported:8')
        Pumps.Ok_Import(self)
        sleep(10)

#----------------------------------- Delete Pump --------------------------------------------------------------------------------------------------------------------------------------

    @data(*read_excel.get_data_from_excel(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +  '\\Data\\pumps.xlsx','Sheet1'))
    @unpack
    def test_delete(self,SN, Type):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        Pumps.Pumps_link(self)
        sleep(3)
        try: Pumps.Select_Pump(self,SN)
        except NoSuchElementException as e:return True
        sleep(3)
        Pumps.Remove_Pump(self)
        sleep(5)

if __name__ == '__main__':
     unittest.main()
    # oneTestCase =  unittest.TestSuite()
    # oneTestCase.addTest(test_Pumps("test_delete"))
    # unittest.TextTestRunner().run(oneTestCase)

