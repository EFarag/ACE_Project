import unittest
from   DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from   Pages.LoginPage import LoginPage
from   BaseTestCases.BaseTestCase import BaseTestCase
from   Pages.DataSet_Import import Dataset
from   Pages.DataSet_Import import Dataset_import
from   Pages.DataSet_Import import Import_Password
from   Pages.DataSet_Import import Upload
from   Pages.DataSet_Import import ID_code
from   Pages.DataSet_Import import Assert_Dataset
from   Pages.DataSet_Import import Popup_Assertion
from   Pages.DataSet_Import import Toast
from selenium.webdriver.common.by import By
from time import sleep



@ddt
class Datasets(BaseTestCase):


   @data(*read_excel.get_data_from_excel('D:\Automation Python\ACE_Project\Data\login_data.xlsx','Datasets'))
   @unpack
   def test_Upload(self,url,code,DatasetName):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(1)
       Dataset.Dataset_link(self)
       self.assertEqual(Assert_Dataset.DS_Assert(self),'Data Sets')
       #Assert that Datasets page is opened
       Dataset_import.Import(self)
       self.assertTrue(Popup_Assertion.is_element_present(self,how=By.CSS_SELECTOR, what='html.firefox-45 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable'))
       #Assert that login password popup screen is displayed
       Import_Password.Password(self,password='P@ssw0rd')
       self.assertTrue(Popup_Assertion.is_element_present(self,how=By.CSS_SELECTOR,what='html.firefox-45 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable'))
        #Assert that Import Dataset popup screen is displayed
       Upload.File_Upload(self,location=url)
       ID_code.Dataset_Import(self,IDC=code)
       sleep(3)
       #Assert that Dataset is added successfully
       self.assertEqual(Toast.Toast_Message(self),"Data Set "+DatasetName+" has been imported.")
       print(Toast.Toast_Message(self))







if __name__ == '__main__':
    unittest.main()