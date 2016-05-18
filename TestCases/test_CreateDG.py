import unittest
from ACE_Project.BaseTestCases.BaseTestCase import BaseTestCase
from ACE_Project.Pages.Deployment_Group import DG_Create
from ACE_Project.Pages.LoginPage import LoginPage
from ACE_Project.DataSource.read_excel import read_excel
from time import sleep
from ddt import ddt,data,unpack


@ddt
class test_DG_Create (BaseTestCase):

    @data(*read_excel.get_data_from_excel('C:/Users/DGad/Desktop/automation/ACE_Project/Data/login_data.xlsx','DG'))
    @unpack

    def test_Create_DG(self,DGname,DGdesc,DGDB):
        LoginPage.login(self,'Administrator','P@ssw0rd')
        sleep(3)
        DG_Create.DG_screenlink(self)
        sleep(3)
        DG_Create.DG_createlink(self)
        sleep(3)
        DG_Create.DG_DetailsPopup(self,DGname,DGdesc,int(DGDB))
        #Actual_Msg = DG_Create.DG_toast
        sleep(3)
        self.assertEqual(DG_Create.Toast(self),"Deployment Group " + DGname + " has been created.")

        # self.assertTrue(DG_Create.DG_toast(DGname))
        #print(DG_Create.DG_toast)


if __name__ == '__main__':
    unittest.main()
