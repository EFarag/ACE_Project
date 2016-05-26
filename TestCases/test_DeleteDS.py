import unittest
from DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.DataSet_Import import Dataset
from time import sleep
import os.path



@ddt
class deleteDS(BaseTestCase):

   @data(*read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx','Datasets_Deletion'))
   @unpack
   def Delete_DSet(self,DS_name):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(3)
       Dataset.Dataset_link(self)
       sleep(3)
       self.assertEqual(Dataset.DS_Assert(self),'Data Sets')
       sleep(3)
       Dataset.Delete_DataSet(self,DS_name)
       sleep(5)
       self.assertEqual(Dataset.Delete_Toast(self),"Data Set ["+DS_name+"] has been deleted.")



if __name__ == '__main__':
    unittest.main()