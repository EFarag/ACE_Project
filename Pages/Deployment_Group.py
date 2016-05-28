#import action as action
import selenium
import select

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from ddt import ddt, data, unpack
import os.path
from DataSource.read_excel import read_excel


@ddt
class DG_Create():
    DG_screen = (By.CSS_SELECTOR,
                 'html.firefox-42 body form#aspnetForm div#wrapper div.home-wrap div.sections div.home-section div#ctl00_MasterPageContent_rptHomeMenu_ctl01_ctl00_ctl02_div_itemSection.item-section div.item-Wrap a#ctl00_MasterPageContent_rptHomeMenu_ctl01_ctl00_ctl02_MenuLink.subsection')

    def DG_screenlink(self):
        self.driver.find_element(*DG_Create.DG_screen).click()

    # Deployment group screen buttons
    CreateDG_btn = (By.ID, 'ctl00_ctl00_MasterPageContent_cpv_lbCreate')

    def DG_createlink(self):
        self.driver.find_element(*DG_Create.CreateDG_btn).click()


    def DG_edit(self):
        self.driver.find_element(*DG_Create.Edit_btn).click()

    # Create Deployment Group popup controls:
    DG_Name = (By.ID, 'ctl00_ctl00_MasterPageContent_cpv_dialogTxtDeploymentGroupName')
    DG_Description = (By.ID, 'ctl00_ctl00_MasterPageContent_cpv_dialogTxtAreaDeploymentGroupDescription')
    DG_DB = (By.ID, 'ctl00_ctl00_MasterPageContent_cpv_cqiDatabaseDropDownList')
    # DG_DB = (By.CSS_SELECTOR,'table tbody tr td select#ctl00_ctl00_MasterPageContent_cpv_cqiDatabaseDropDownList')
    DG_SaveConBtn = (By.XPATH, '/html/body/div[3]/div[3]/div/button[1]')
    DG_SaveCloseBtn = (By.XPATH, '/html/body/div[3]/div[3]/div/button[2]')
    DG_CancelBtn = (By.XPATH, '/html/body/div[3]/div[3]/div/button[3]')
    DG_toast = (By.CSS_SELECTOR, 'html.firefox-42 body div.blockUI.toast.blockPage')
    Name_req = (By.XPATH, ".//*[@id='ctl00_ctl00_MasterPageContent_cpv_labelDeploymentGroupNameRequired']")
    Desc_req = (By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_labelAreaDeploymentGroupDescriptionRequired']")
    DB_req = (By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_cqiDatabaseSelectionRequired']")
    DuplicateDG_msg=(By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_labelDGAlreadyUsedText']")
    # DG popup functions
    def DG_DetailsPopup(self, name, desc, index):
        self.driver.find_element(*DG_Create.DG_Name).send_keys(name)
        sleep(3)
        self.driver.find_element(*DG_Create.DG_Description).send_keys(desc)
        DGDB_DDL = Select(self.driver.find_element(*DG_Create.DG_DB))
        print(len(DGDB_DDL.options))
        DGDB_DDL.select_by_index(index)
        sleep(3)
        self.driver.implicitly_wait(10)

    def save_close_btn(self):
        self.driver.find_element(*DG_Create.DG_SaveCloseBtn).click()
        self.driver.implicitly_wait(10)

    def save_cont_btn(self):
        self.driver.find_element(*DG_Create.DG_SaveConBtn).click()

    def Cancel(self):
        self.driver.find_element(*DG_Create.DG_CancelBtn).click()

    #Functions that return error message might displayed while creating DG
    def DuplicateDG(self):
        Duplicate_error=self.driver.find_element(*DG_Create.DuplicateDG_msg).text
        return Duplicate_error

    def ReqName(self):
        ReqName_error = self.driver.find_element(*DG_Create.Name_req).text
        return ReqName_error

    def ReqDesc(self):
        ReqDesc_error = self.driver.find_element(*DG_Create.Desc_req).text
        return ReqDesc_error

    def ReqDB(self):
        ReqDB_error = self.driver.find_element(*DG_Create.DB_req).text
        return ReqDB_error

    # DG Toast message
    def Toast(self):
        Label_TXT = self.driver.find_element(*DG_Create.DG_toast).text
        return Label_TXT


    # Create DG popup appearance assertion
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_element_disabled(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return True
        if True:
            return False

        else:
            print('Test Failed')

            ###Delete DG###

            # Deployment Group Delete popup

    Delete_popup = (By.CSS_SELECTOR, '#popup-deleteDeploymentGroup')
    Delete_warning = (By.CSS_SELECTOR, '#ctl00_ctl00_MasterPageContent_cpv_labelDeleteWarning')
    Delete_con_btn = (By.CSS_SELECTOR, '.ui-button.ui-widget.ui-state-default.ui-corner-all.ui-button-text-only.ui-state-focus')
    Confirm_deletionPassword = (By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_tbPassword']")
    Delete_btn = (By.XPATH, 'html/body/div[4]/div[3]/div/button[1]')

    # This function is to select deployment group created in prev TC and delete them
    DGGrid = (By.XPATH, ".//*[@id='ctl00_ctl00_MasterPageContent_cpv_lstDeploymentGroups_itemPlaceholderContainer']/tbody/tr")
    def AselectDG(self, name):
        options_List = []
        options_List = self.driver.find_elements(*DG_Create.DGGrid)
        options_List.pop(0)
        for option in options_List:
            groupName = option.find_element(By.XPATH, ".//td[1]").text
            if groupName == name:
                CB = option.find_element(By.XPATH, ".//td[1]/span")
                CB.click()
                break

                # Click on delete button

    def DG_delete(self):
        delete = WebDriverWait(self.driver, 10) \
            .until(expected_conditions.
                   visibility_of_element_located
                   ((By.CSS_SELECTOR, '#ctl00_ctl00_MasterPageContent_cpv_lbDelete')))
        delete.click()

    def DG_edit(self):
        Edit_btn = WebDriverWait(self.driver, 10) \
            .until(expected_conditions.
                   visibility_of_element_located
                   ((By.XPATH, ".//*[@id='ctl00_ctl00_MasterPageContent_cpv_lbEdit']")))
        Edit_btn.click()

    # This function is to return warning message before deployment group deletion inorder to assert it in the test case
    def warning_delete(self):
        Warning_text = self.driver.find_element(*DG_Create.Delete_warning).text
        return Warning_text

    # This function is to click on continue deletion button
    def complete_delete1(self):
        WebDriverWait(self.driver, 10) \
            .until(expected_conditions.visibility_of_element_located,
                   ((By.CSS_SELECTOR, "#popup-deleteDeploymentGroup")))
        self.driver.find_element(*DG_Create.Delete_con_btn).click()
        WebDriverWait(self.driver, 20) \
            .until(expected_conditions.visibility_of_element_located,
                   ((By.CSS_SELECTOR, "#ctl00_ctl00_MasterPageContent_cpv_tbPassword")))
     # DG Toast message
    def confirm_Delete(self):
        confirm_delete_msg = self.driver.find_element(By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_labelDeletePassword']").text
        return confirm_delete_msg

    def complete_delete2(self):
        self.driver.find_element(*DG_Create.Confirm_deletionPassword).send_keys("P@ssw0rd")
        self.driver.implicitly_wait(5)
        WebDriverWait(self.driver, 30) \
            .until(expected_conditions.visibility_of_element_located,
                   ((By.CSS_SELECTOR, "html/body/div[4]/div[3]/div/button[1]")))
        self.driver.implicitly_wait(5)
        delButton = self.driver.find_element(*DG_Create.Delete_btn)
        delButton.click()

# This function is to set login password to complete deletion and then click on delete button
