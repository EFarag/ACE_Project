import unittest
from ACE_Project.BaseTestCases.BaseTestCase import BaseTestCase
from ACE_Project.Pages.Deployment_Group import DG_Create
from ACE_Project.Pages.LoginPage import LoginPage
from time import sleep
import select



class test_DG_Create (BaseTestCase):
    def test_Create_DG(self):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        DG_Create.DG_screenlink(self)
        sleep(3)
        DG_Create.DG_createlink(self)
        sleep(3)
        DG_Create.DG_DetailsPopup(self)
        sleep(10)
if __name__ == '__main__':
    unittest.main()
