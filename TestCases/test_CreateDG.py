import unittest
from ACE_Project.BaseTestCases.BaseTestCase import BaseTestCase
from ACE_Project.Pages.Deployment_Group import DG_Create
from ACE_Project.Pages.LoginPage import LoginPage
from time import sleep
import select
from ddt import ddt,data,unpack



class test_DG_Create (BaseTestCase):

   @data(*read_excel.get_data_from_excel('C:/Users/DGad/Desktop/automation/ACE_Project/Data/login_data.xlsx','DG'))
   @unpack

    def test_Create_DG(self,DGname,DGdesc):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        DG_Create.DG_screenlink(self)
        sleep(3)
        DG_Create.DG_createlink(self)
        sleep(3)
        DG_Create.DG_DetailsPopup(self,,)
        sleep(10)
        self.assertEqual(DG_Create.DG_toast(self),"Deployment Group Group1 has been created.")
        print(DG_Create.DG_toast(self))
if __name__ == '__main__':
    unittest.main()
