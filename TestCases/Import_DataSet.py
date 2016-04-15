import unittest

#from ddt import ddt,data,unpack
from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.DataSet_Import import Dataset
from Pages.DataSet_Import import Dataset_import
from Pages.DataSet_Import import Import_Password
from Pages.DataSet_Import import Upload
from Pages.DataSet_Import import Submit
from time import sleep



#@ddt
class LoginTest(BaseTestCase):


    def test_login_with_valid_credentials(self):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(1)
       Dataset.Dataset_link(self)
       Dataset_import.Import(self)
       Import_Password.Password(self,password='P@ssw0rd')
       Upload.File_Upload(self,location='C:/VP Only 4DE7.mgr')
       Submit.Submit_upload(self)
       sleep(3)
if __name__ == '__main__':
    unittest.main()