import unittest

from ddt import ddt,data,unpack
from selenium import webdriver
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from BaseTestCases.BaseTestCase import BaseTestCase
from DataSource.read_excel import read_excel
from time import sleep
import os.path


@ddt
class LoginTest(BaseTestCase):


    @data(*read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx','login'))
    @unpack
    def test_login(self,Username,Password,LoginName):
       self.driver.implicitly_wait(30)
       LoginPage.clear_Credentials(self)
       LoginPage.login(self,Username,Password)

       if(Username == ""):
        sleep(5)
        self.assertEqual(LoginPage.Username_required(self),"* Required")

       elif(Password == ""):
        sleep(5)
        self.assertEqual(LoginPage.Password_required(self),"* Required")

       elif(Username !="Administrator" or Password != "P@ssw0rd"):
        sleep(5)
        self.assertEqual(LoginPage.Invalid_login(self),"Username and/or password is incorrect. For help, contact your administrator.")
       else:
        sleep(3);
        self.assertEqual(LoginName,HomePage.get_login_name(self))
        print(HomePage.get_login_name(self))





if __name__ == '__main__':
    unittest.main()
