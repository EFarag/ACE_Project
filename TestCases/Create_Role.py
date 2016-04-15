import unittest

#from ddt import ddt,data,unpack
from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.CreateRole import RolesPage
from time import sleep



#@ddt
class LoginTest(BaseTestCase):


    def test_login_with_valid_credentials(self):
       LoginPage.login(self,'Administrator','P@ssw0rd')
       sleep(1)
       RolesPage.Roles(self)

if __name__ == '__main__':
    unittest.main()