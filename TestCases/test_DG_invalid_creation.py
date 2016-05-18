import unittest
from ACE_Project.BaseTestCases.BaseTestCase import BaseTestCase
from ACE_Project.Pages.Deployment_Group import DG_Create

from ACE_Project.Pages.LoginPage import LoginPage
from time import sleep
from selenium.webdriver.common.by import By

class test_initialize(BaseTestCase):

      def test_name_req(self):
        #Assert that "* Required" error is displayed when DG name is empty
         LoginPage.login(self,'Administrator','P@ssw0rd')
         sleep(3)
         DG_Create.DG_screenlink(self)
         sleep(3)
         DG_Create.DG_createlink(self)
         sleep(3)
         self.assertTrue(DG_Create.is_element_present(self,how=By.CSS_SELECTOR, what='html.firefox-42 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable'))
         sleep(3)
         DG_Create.DG_DetailsPopup(self,'','desc',1)
         sleep(3)
         Name_req_msg = DG_Create.ReqName(self)
         print( Name_req_msg)
         self.assertEqual( Name_req_msg,"* Required")
         DG_Create.Cancel(self)
         #self.assertFalse(DG_Create.is_element_present(self,how=By.CSS_SELECTOR, what='html.firefox-42 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable'))


        #Assert that "* Required" error is displayed when DG Desc is empty
         DG_Create.DG_createlink(self)
         sleep(3)
         self.assertTrue(DG_Create.is_element_present(self,how=By.CSS_SELECTOR, what='html.firefox-42 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable'))
         sleep(3)
         DG_Create.DG_DetailsPopup(self,'DG_name','',1)
         sleep(3)
         Desc_req_msg = DG_Create.ReqDesc(self)
         print( Desc_req_msg)
         self.assertEqual( Desc_req_msg,"* Required")
         DG_Create.Cancel(self)

        #Assert that "* Required" error is displayed when DG DB is empty
         DG_Create.DG_createlink(self)
         sleep(3)
         self.assertTrue(DG_Create.is_element_present(self,how=By.CSS_SELECTOR, what='html.firefox-42 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable'))
         sleep(3)
         DG_Create.DG_DetailsPopup(self,'DG_name','DG_desc',0)
         sleep(3)
         DB_req_msg = DG_Create.ReqDB(self)
         print( DB_req_msg)
         self.assertEqual( DB_req_msg,"* Required")
         DG_Create.Cancel(self)

        #Assert that "* Required" error is displayed when All DG details are empty
         DG_Create.DG_createlink(self)
         sleep(3)
         self.assertTrue(DG_Create.is_element_present(self,how=By.CSS_SELECTOR, what='html.firefox-42 body div.ui-dialog.ui-widget.ui-widget-content.ui-corner-all.ui-front.ui-dialog-buttons.ui-draggable'))
         sleep(3)
         DG_Create.DG_DetailsPopup(self,'','',0)
         sleep(3)
         DB_req_msg = DG_Create.ReqDB(self)
         Name_req_msg = DG_Create.ReqName(self)
         Desc_req_msg = DG_Create.ReqDesc(self)
         print( Name_req_msg)
         self.assertEqual( Name_req_msg,"* Required")
         print( Desc_req_msg)
         self.assertEqual( Desc_req_msg,"* Required")
         print( DB_req_msg)
         self.assertEqual( DB_req_msg,"* Required")
         DG_Create.Cancel(self)
if __name__ == '__main__':
    unittest.main()