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


class DG_validEdit(BaseTestCase):
    def test_valid_DG_Edit(self):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        DG_Create.DG_screenlink(self)
        sleep(3)
        DG_Create.AselectDG(self,'Group2')
        self.assertTrue(DG_Details.screen_displayed(self,how=By.XPATH,what=".//*[@id='ctl00_ctl00_MasterPageContent_cpv_lbEdit']"))
        sleep(3)
        DG_Create.DG_edit(self)
        sleep(3)
        self.assertTrue(DG_Details.screen_displayed(self,how=By.XPATH,what=".//*[@id='ctl00_ctl00_MasterPageContent_cpv_lbReturnToList']"))
        #Assert that updating DG Name with name that does`nt exist will be allowed
        DG_Details.Edit_name_link(self)
        sleep(3)
        DG_Details.clear_DGName(self)
        sleep(3)
        DG_Details.edit_name(self,'Group2_new')
        sleep(3)
        DG_Details.edit_desc(self,'Group2_new')
        sleep(3)
        DG_Details.save_btn(self)
        sleep(3)
        self.assertEqual(DG_Details.Toast(self),"Deployment Group Group2 has been edited.")


if __name__ == '__main__':
    unittest.main()
