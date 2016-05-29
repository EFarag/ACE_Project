import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from BaseTestCases.BaseTestCase import BaseTestCase
from Pages.Deployment_Group import DG_Create
from Pages.LoginPage import LoginPage
from time import sleep

class test_invalid_create(BaseTestCase):
      def test_name_req(self):
         self.driver.implicitly_wait(30)
         LoginPage.login(self,'Administrator','P@ssw0rd')
         sleep(3)
         DG_Create.DG_screenlink(self)
         sleep(3)
        #Assert that "* Required" error is displayed when DG DB is empty
         DG_Create.DG_createlink(self)
         sleep(3)
         DG_Create.DG_DetailsPopup(self,'Group1','DG_desc',1)
         sleep(3)
         DG_Create.save_close_btn(self)
         sleep(3)
         DG_Duplicate = DG_Create.DuplicateDG(self)
         print(DG_Duplicate)
         self.assertEqual(DG_Duplicate,"Deployment Group Name is already used.")
         DG_Create.Cancel(self)

        #Assert that "* Required" error is displayed when DG name is empty
         DG_Create.DG_createlink(self)
         sleep(3)
         DG_Create.DG_DetailsPopup(self,'','desc',1)
         sleep(3)
         DG_Create.save_close_btn(self)
         sleep(3)
         Name_req_msg =DG_Create.ReqName(self)
         print(Name_req_msg)
         self.assertEqual(Name_req_msg,"* Required")
         DG_Create.Cancel(self)

        #Assert that "* Required" error is displayed when DG Desc is empty
         DG_Create.DG_createlink(self)
         sleep(3)
         DG_Create.DG_DetailsPopup(self,'DG_name','',1)
         sleep(3)
         DG_Create.save_close_btn(self)
         sleep(3)
         Desc_req_msg = DG_Create.ReqDesc(self)
         print( Desc_req_msg)
         self.assertEqual( Desc_req_msg,"* Required")
         DG_Create.Cancel(self)

        #Assert that "* Required" error is displayed when DG DB is empty
         DG_Create.DG_createlink(self)
         sleep(3)
         DG_Create.DG_DetailsPopup(self,'DG_name','DG_desc',0)
         sleep(3)
         DG_Create.save_close_btn(self)
         sleep(3)
         DB_req_msg = DG_Create.ReqDB(self)
         print(DB_req_msg)
         self.assertEqual(DB_req_msg,"* Required")
         DG_Create.Cancel(self)

        #Assert that "* Required" error is displayed when All DG details are empty
         DG_Create.DG_createlink(self)
         sleep(3)
         DG_Create.DG_DetailsPopup(self,'','',0)
         sleep(3)
         DG_Create.save_close_btn(self)
         sleep(3)
         DB_req_msg = DG_Create.ReqDB(self)
         sleep(3)
         Name_req_msg = DG_Create.ReqName(self)
         sleep(3)
         Desc_req_msg = DG_Create.ReqDesc(self)
         sleep(3)
         print( Name_req_msg)
         self.assertEqual( Name_req_msg,"* Required")
         print( Desc_req_msg)
         self.assertEqual( Desc_req_msg,"* Required")
         print(DB_req_msg)
         self.assertEqual(DB_req_msg,"* Required")
         DG_Create.Cancel(self)

if __name__ == '__main__':
    unittest.main()