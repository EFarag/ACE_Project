import unittest
from  DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.Roles import RolesPage
from time import sleep
import os.path



@ddt
class Roles_Delete(BaseTestCase):

   @data(*read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx','Roles_Deletion'))
   @unpack
   def test_Create_Roles(self,Role_name):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(3)
       RolesPage.Roles(self)
       sleep(3)
       RolesPage.Role_Delete(self,Role_name)
       sleep(5)
       self.assertEqual(RolesPage.DeleteRole_Message(self),"Role "+Role_name+" has been deleted.")



if __name__ == '__main__':
    unittest.main()