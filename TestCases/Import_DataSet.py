import unittest
from DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.DataSet_Import import Dataset
from Pages.DataSet_Import import Dataset_import
from Pages.DataSet_Import import Import_Password
from Pages.DataSet_Import import Upload
from Pages.DataSet_Import import ID_code
from time import sleep



@ddt
class LoginTest(BaseTestCase):


   @data(*read_excel.get_data_from_excel('C:/Users/aabdelhamid/PycharmProjects/ACE_Project-master/Data/login_data.xlsx','Datasets'))
   @unpack
   def test_Upload(self,url,code):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(1)
       Dataset.Dataset_link(self)
       Dataset_import.Import(self)
       Import_Password.Password(self,password='P@ssw0rd')
       Upload.File_Upload(self,location=url)
       ID_code.Dataset_Import(self,IDC=code)
       sleep(3)



if __name__ == '__main__':
    unittest.main()