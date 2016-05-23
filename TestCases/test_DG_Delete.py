import unittest
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.Deployment_Group import DG_Create
from Pages.LoginPage import LoginPage
from Pages.DG_details_Screen import DG_Details
from time import sleep
from selenium.webdriver.common.by import By

class test_DGDelete(BaseTestCase):
    def test_Delete_DG(self):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        DG_Create.DG_screenlink(self)
        sleep(3)
        DG_Create.DG_CB(self)
        self.assertTrue(DG_Details.screen_displayed(self,how=By.CSS_SELECTOR,what='#ctl00_ctl00_MasterPageContent_cpv_lbDelete'))
        self.driver.implicitly_wait(10)
        sleep(10)
        DG_Create.DG_delete(self)
        sleep(3)
        self.assertTrue(DG_Details.screen_displayed(self,how=By.CSS_SELECTOR,what='#popup-deleteDeploymentGroup'))
        sleep(3)
        self.assertTrue(DG_Details.screen_displayed(self,how=By.CSS_SELECTOR,what='#ui-id-3'))

if __name__ == '__main__':
    unittest.main()
