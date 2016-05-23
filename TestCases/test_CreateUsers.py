import unittest
from ddt import ddt,data,unpack
from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.UsersPage import UsersPage
from time import sleep
from DataSource.read_excel import read_excel
from Pages.UsersPage import Add_Users


@ddt
class LoginTest(BaseTestCase):


    #def test_login_with_valid_credentials(self):
      # LoginPage.login(self,'Administrator','P@ssw0rd')
       #sleep(1)
       #UsersPage.Users(self)



    @data(*read_excel.get_data_from_excel('C:/Users/DGad/Desktop/automation/ACE_Project/Data/Test_Data.xlsx','users'))
    @unpack
    def test_Enter_Users(self,first_name,last_name,user_name,password,re_password):
         LoginPage.login(self,'Administrator','P@ssw0rd')
         sleep(2);
         UsersPage.Users(self)
         sleep(2);
         Add_Users.Multi_Users(self,first_name,last_name,user_name,password,re_password)
         sleep(5);


if __name__ == '__main__':
    unittest.main()
