import unittest

from ddt import ddt,data,unpack
from selenium import webdriver
from ACE_Project.Pages.HomePage import HomePage
from ACE_Project.Pages.LoginPage import LoginPage
from ACE_Project.BaseTestCases.BaseTestCase import BaseTestCase
from ACE_Project.DataSource.read_excel import read_excel
from time import sleep


@ddt
class LoginTest(BaseTestCase):


    @data(*read_excel.get_data_from_excel('C:/Users/efarrag/PycharmProjects/ACE_Project/ACE_Project/Data/login_data.xlsx','login'))
    @unpack
    def test_login_with_valid_credentials(self,Username,Password,LoginName):
       LoginPage.login(self,Username,Password)
       sleep(3);
       self.assertEqual(LoginName,HomePage.get_login_name(self))
       print(HomePage.get_login_name(self))




if __name__ == '__main__':
    unittest.main()
