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
class Roles(BaseTestCase):

   @data(*read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx','Roles'))
   @unpack
   def test_Create_Roles(self,Role_name,Role_Perm):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(3)

       RolesPage.Roles(self)
       sleep(3)
       RolesPage.btn_Create(self)
       sleep(2)
       RolesPage.Role_name_Creation(self,Role_name)
       RolesPage.Select_Permissions(self,Role_Perm)
       sleep(5)
       RolesPage.Move_Left(self)
       RolesPage.Save_Role(self)
       if Role_name == "":
        self.assertTrue(RolesPage.Role_name_missing(self),"* Required")
       else:
        self.assertEqual(RolesPage.Role_Message(self),"Role "+Role_name+" has been created.")
        print(RolesPage.Role_Message(self))



if __name__ == '__main__':
    unittest.main()