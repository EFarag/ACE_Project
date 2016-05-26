import unittest
from ddt import ddt, data, unpack
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from BaseTestCases.BaseTestCase import BaseTestCase, os
from DataSource.read_excel import read_excel
from Pages.DG_details_Screen import DG_Details
from Pages.Deployment_Group import DG_Create
from Pages.LoginPage import LoginPage
from time import sleep
import os.path

class Assign_DS(BaseTestCase):
    def test_AssignDS(self):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        DG_Create.DG_screenlink(self)
        sleep(3)
        DG_Create.AselectDG(self,'Group2')
        sleep(3)
        DG_Create.DG_edit(self)
        sleep(5)
        self.assertTrue(DG_Details.screen_displayed(self,how=By.XPATH,what=".//*[@id='ctl00_ctl00_MasterPageContent_cpv_lbReturnToList']"))
        sleep(3)
        DG_Details.AssignDS_button(self)
        sleep(3)
        DG_Details.AssignDataset(self,'P@ssw0rd','Maxi - v3 - A3AA','A3AA')
        sleep(10)
        self.assertEqual(DG_Details.Toast(self),"Maxi has been assigned to [Group2].")

if __name__ == '__main__':
    unittest.main()


