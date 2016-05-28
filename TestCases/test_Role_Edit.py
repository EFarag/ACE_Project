import unittest
from  DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.Roles import RolesPage
from time import sleep
from selenium.webdriver.common.by import By
import os.path



@ddt
class Roles_Edit(BaseTestCase):

   @data(*read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx','Roles_Editing'))
   @unpack
   def test_Create_Roles(self,Role_name,Role_Perm):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(3)
       RolesPage.Roles(self)
       sleep(3)
       RolesPage.Role_Edit(self,Role_name,Role_Perm)
       sleep(3)
       self.assertEqual(RolesPage.UpdateRole_Message(self),"Role "+Role_name+" has been updated.")



if __name__ == '__main__':
    unittest.main()