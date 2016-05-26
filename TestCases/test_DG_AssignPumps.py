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
from Pages.Pumps import Pumps
import os.path

@ddt
class AssignPumps(BaseTestCase):
    @data(*read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx','Assign_to_DG'))
    @unpack
    def test_DG_AssignPmps(self,filename):

        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        DG_Create.DG_screenlink(self)
        sleep(3)
        File_location = os.path.join(os.path.dirname(__file__), os.pardir) +  '\Data\\' + filename
        print(File_location)
        DG_Create.AselectDG(self,'Group2')
        sleep(3)
        DG_Create.DG_edit(self)
        sleep(5)
        self.assertTrue(DG_Details.screen_displayed(self,how=By.XPATH,what=".//*[@id='ctl00_ctl00_MasterPageContent_cpv_lbReturnToList']"))
        sleep(3)
        DG_Details.Assignpmp(self)
        self.assertTrue(DG_Details.screen_displayed(self,how=By.XPATH,what=".//*[@id='divImportPump']"))
        sleep(3)
        Pumps.Browse_File(self,File_location)
        sleep(3)
        DG_Details.cont_pmp_assign(self)

if __name__ == '__main__':
    unittest.main()
