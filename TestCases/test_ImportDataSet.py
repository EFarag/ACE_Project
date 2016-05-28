import unittest
from DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.DataSet_Import import Dataset
from Pages.DataSet_Import import Popup_Assertion
from selenium.webdriver.common.by import By
from time import sleep
import os.path



@ddt
class Datasets(BaseTestCase):


   @data(*read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx','Datasets'))
   @unpack
   def test_Upload(self,DatasetName,code):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(1)
       Dataset.Dataset_link(self)
       self.assertEqual(Dataset.DS_Assert(self),'Data Sets')
       #Assert that Datasets page is opened
       Dataset.Import(self)
       sleep(5)
       self.assertTrue(Popup_Assertion.is_element_present(self,how=By.XPATH, what=".//*[@id='ctl00_ctl00_MasterPageContent_cpv_txtActionPassword']"))
       #Assert that login password popup screen is displayed
       Dataset.Password(self,password='P@ssw0rd')
       sleep(5)
       self.assertTrue(Popup_Assertion.is_element_present(self,how=By.XPATH,what=".//*[@id='ui-id-3']"))
        #Assert that Import Dataset popup screen is displayed
       url = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\\'+DatasetName
       Dataset.File_Upload(self,location= url)
       if url == "":
        sleep(5)
         #Assert that Import Dataset file name is required
        self.assertEqual(Dataset.Required_filename(self),"File Name is required.")
       elif DatasetName[-4:] != ".mgr":
        sleep(5)
        #Assert that Import Dataset file type should be .mgr only is required
        self.assertEqual(Dataset.Invalid_file(self),"Only .mgr files are allowed.")
       else:
        Dataset.Dataset_Import(self,IDC=code)
        sleep(5)
       #Assert that Dataset is added successfully
        self.assertEqual(Dataset.Toast_Message(self),"Data Set "+DatasetName+" has been imported.")
        print(Dataset.Toast_Message(self))







if __name__ == '__main__':
    unittest.main()