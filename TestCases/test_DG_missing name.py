import unittest
from ACE_Project.BaseTestCases.BaseTestCase import BaseTestCase
from ACE_Project.Pages.Deployment_Group import DG_Create
from ACE_Project.Pages.LoginPage import LoginPage
from time import sleep


class DgDesc(BaseTestCase):

      def test_missing_name(self):
         LoginPage.login(self,'Administrator','P@ssw0rd')
         sleep(3)
         DG_Create.DG_screenlink(self)
         sleep(3)
         DG_Create.DG_createlink(self)
         sleep(3)
         DG_Create.DG_DetailsPopup(self,'','desc',1)
         sleep(3)
         req_msg = DG_Create.ReqName(self)
         print(req_msg)
         self.assertEqual(req_msg,"* Required")

if __name__ == '__main__':
    unittest.main()