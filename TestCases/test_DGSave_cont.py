import unittest
from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.Deployment_Group import DG_Create
from Pages.DG_details_Screen import DG_Details
from Pages.LoginPage import LoginPage
from Pages.Pumps import Pumps
import os.path
from DataSource.read_excel import read_excel
from selenium.webdriver.common.by import By
from time import sleep
from ddt import ddt,data,unpack


@ddt
class test_DG_Creation (BaseTestCase):

    @data(*read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx','DG'))
    @unpack

    def test_Create_DG(self,DGname,DGdesc,DGDB):
        self.driver.implicitly_wait(30)
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        DG_Create.DG_screenlink(self)
        sleep(3)
        DG_Create.DG_createlink(self)
        sleep(3)
        DG_Create.DG_DetailsPopup(self,DGname,DGdesc,int(DGDB))
        #Actual_Msg = DG_Create.DG_toast
        DG_Create.save_cont_btn(self)
        sleep(3)
        #self.assertEqual(DG_Create.Toast(self),"Deployment Group " + DGname + " has been created.")
        # self.assertTrue(DG_Create.DG_toast(DGname))
        #print(DG_Create.DG_toast)
        self.assertTrue(DG_Details.screen_displayed(self,how=By.CSS_SELECTOR,what='#ctl00_ctl00_MasterPageContent_cpv_lbReturnToList'))


if __name__ == '__main__':
    unittest.main()