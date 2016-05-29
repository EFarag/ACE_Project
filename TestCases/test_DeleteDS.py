import unittest
from DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.DataSet_Import import Dataset
from time import sleep
import os.path



@ddt
class Delete_Dataset(BaseTestCase):

   @data(*read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx','Datasets_Deletion'))
   @unpack
   def test_DeleteDS(self,DS_name, DS_Code):
       self.driver.implicitly_wait(30)
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(15)
       Dataset.Dataset_link(self)
       sleep(3)
       self.assertEqual(Dataset.DS_Assert(self),'Data Sets')
       sleep(3)
       Dataset.Delete_DataSet(self,DS_name)
       Dataset.Password(self,"P@ssw0rd")
       sleep(5)
       Dataset.Dataset_Delete_code(self,DS_Code)
       sleep(30)
       self.assertEqual(Dataset.Delete_Toast(self),"Data Set ["+DS_name+"] has been deleted.")



if __name__ == '__main__':
    unittest.main()