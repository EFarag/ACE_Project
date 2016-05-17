import unittest
from  DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from  Pages.LoginPage import LoginPage
from  BaseTestCases.BaseTestCase import BaseTestCase
from  Pages.CreateRole import RolesPage
from  Pages.CreateRole import Create
from  Pages.CreateRole import Role_Creation
from  Pages.CreateRole import Create_Role_MSG
from time import sleep



@ddt
class Roles(BaseTestCase):

   @data(*read_excel.get_data_from_excel('D:\Automation Python\ACE_Project\Data\login_data.xlsx','Roles'))
   @unpack
   def test_Create_Roles(self,Role_name):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(3)
       RolesPage.Roles(self)
       sleep(3)
       Create.btn_Create(self)
       sleep(2)
       Role_Creation.Role(self,Role_name)
       sleep(3)
       self.assertEqual(Create_Role_MSG.Role_Message(self),"Role "+Role_name+" has been created.")
       print(Create_Role_MSG.Role_Message(self))

if __name__ == '__main__':
    unittest.main()