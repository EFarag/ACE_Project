import unittest
from BaseTestCases.BaseTestCase import BaseTestCase
from DataSource.read_excel import read_excel
from Pages.Deployment_Group import DG_Create
from Pages.LoginPage import LoginPage
from Pages.DG_details_Screen import DG_Details
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ddt import ddt,data,unpack
import os.path

@ddt
class test_DGDelete(BaseTestCase):

    @data(*read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx','DG_delete'))
    @unpack
    def test_Delete_DG(self,DGname):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        DG_Create.DG_screenlink(self)
        sleep(3)
        #DG_Create.DG_CB(self)
        DG_Create.AselectDG(self,DGname)
        self.assertTrue(DG_Details.screen_displayed(self,how=By.CSS_SELECTOR,what='#ctl00_ctl00_MasterPageContent_cpv_lbDelete'))
        self.driver.implicitly_wait(10)
        sleep(10)
        DG_Create.DG_delete(self)
        sleep(3)
        #Explicit wait until delete DG warning popup is displayed
        WebDriverWait(self.driver, 10)\
            .until(expected_conditions.visibility_of_element_located,((By.CSS_SELECTOR,"#popup-deleteDeploymentGroup")))
        self.assertTrue(DG_Details.screen_displayed(self,how=By.CSS_SELECTOR,what='#popup-deleteDeploymentGroup'))
        sleep(3)
        WebDriverWait(self.driver, 20)\
            .until(expected_conditions.visibility_of_element_located,((By.CSS_SELECTOR,"#ui-id-3")))
        self.driver.implicitly_wait(5)
        DG_Create.complete_delete1(self)
        #Assert that confirmation message is displayed containing DG name and asking user to enter login password
        self.assertEqual(DG_Create.confirm_Delete(self),"Please enter login password to delete ["+DGname+"]:")
        DG_Create.complete_delete2(self)

        #Assert that toast message is displayed stating that DG has been deleted and DG name is mentioned in the toast message
        sleep(3)
        self.assertEqual(DG_Create.Toast(self),"["+DGname+"]" + " has been deleted.")

if __name__ == '__main__':
    unittest.main()




























