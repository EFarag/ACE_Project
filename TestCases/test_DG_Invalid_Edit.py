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


class DG_InvalidEdit(BaseTestCase):


    def test_Invalid_DG_Edit(self):
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
        #Assert that  error is displayed when DG name is duplicate to another one &that error is displayed when DG name is empty after edit
         DG_Details.Edit_name_link(self)
         sleep(3)
         DG_Details.clear_DGName(self)
         sleep(3)
         Missingname=DG_Details.empty_DG_name(self)
         print(Missingname)
         self.assertEqual(Missingname,"* Required")
         sleep(3)
         DG_Details.edit_name(self,'Group1')
         sleep(3)
         DG_Details.save_btn(self)
         sleep(3)
         DuplicateDG = DG_Details.DuplicateDGname(self)
         print(DuplicateDG)
         self.assertEqual(DuplicateDG,"Deployment Group Name is already used.")
         DG_Details.Cancel(self)
         # Assert that error is displayed when DG Description is empty after edit
         DG_Details.Edit_name_link(self)
         sleep(3)
         DG_Details.clear_desc(self)
         sleep(3)
         DG_Details.save_btn(self)
         sleep(3)
         missingdesc=DG_Details.empty_DG_Des(self)
         print(missingdesc)
         self.assertEqual(missingdesc,"* Required")




if __name__ == '__main__':
    unittest.main()
