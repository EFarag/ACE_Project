import unittest
from DataSource.read_excel import read_excel
from ddt import ddt,data,unpack
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.CreateRole import RolesPage
from Pages.CreateRole import Create
from Pages.CreateRole import Role_Creation
from Pages.CreateRole import Create_Role_MSG
from time import sleep



@ddt
class Roles(BaseTestCase):

   @data(*read_excel.get_data_from_excel('C:/Users/efarrag/PycharmProjects/ACE_Project/ACE_Project/Data/login_data.xlsx','Roles'))
   @unpack
   def test_Create_Roles(self,Role_name):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(1)
       RolesPage.Roles(self)
       Create.btn_Create(self)
       Role_Creation.Role(self,Role_name)
       self.assertEqual(Create_Role_MSG.Role_Message(self),"Role "+Role_name+" has been created.")
       print(Create_Role_MSG.Role_Message(self))

if __name__ == '__main__':
    unittest.main()