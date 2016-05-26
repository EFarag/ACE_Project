import unittest
from ddt import ddt,data,unpack
from selenium import webdriver
from  Pages.HomePage import HomePage
from  Pages.LoginPage import LoginPage
from  BaseTestCases.BaseTestCase import BaseTestCase
from  Pages.UsersPage import Users
from time import sleep
from  DataSource.read_excel import read_excel
from selenium.common.exceptions import NoSuchElementException


@ddt
class test_users(BaseTestCase):



#---------------- Create User ---------------------------------------------------------------------------------------------
    # @data(*read_excel.get_data_from_excel('D:\Automation Python\ACE_Project\Data\login_data.xlsx','users'))
    # @unpack
    # def test_CreateUser(self,first_name,last_name,title,role,user_name,password,re_password, language):
    #      LoginPage.login(self,'Administrator','P@ssw0rd')
    #      sleep(2);
    #      Users.Users_Link(self)
    #      sleep(2);
    #      Users.Create_Link(self)
    #      Users.CreateUsers(self,first_name,last_name,title,role,user_name,password,re_password,language)
    #      sleep(3);
    #      self.assertEqual(Users.PopUpAssertion_LBL(self),"Create User - " +user_name)
    #      self.assertEqual(Users.PopUpAssertion_Body(self),"User " +user_name + " has been created.")
    #      Users.OK(self)
    #      sleep(2)

# #---------------- Delete User ---------------------------------------------------------------------------------------------
    @data(*read_excel.get_data_from_excel('D:\Automation Python\ACE_Project\Data\login_data.xlsx','users'))
    @unpack

    def test_DeleteUser(self,first_name,last_name,title,role,user_name,password,re_password, language):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(2);
        Users.Users_Link(self)
        sleep(2);
        try: Users.Select_User(self,first_name)
        except NoSuchElementException as e:return True
        sleep(3)
        Users.Remove_User(self)



if __name__ == '__main__':
    unittest.main()
