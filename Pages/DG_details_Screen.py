import selenium
import select
from selenium.webdriver.common.by import By
from time import sleep

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class DG_Details():
    ReturnToDG_btn= (By.CSS_SELECTOR,'#ctl00_ctl00_MasterPageContent_cpv_lbReturnToList')
    def returnDG(self):
        self.driver.find_element(*DG_Details.ReturnToDG_btn).click()
    Edit_link=(By.XPATH,".//*[@id='linkDGEdit']")
    def Edit_name_link(self):
        self.driver.find_element(*DG_Details.Edit_link).click()
#Assign Dataset button
    DS_btn=(By.ID,"buttonUpdateDS")
    def AssignDS_button(self):
       # WebDriverWait(self.driver, 10)\
           # .until(expected_conditions.visibility_of_element_located,((By.XPATH,".//*[@id='buttonUpdateDS']")))
        self.driver.find_element(*DG_Details.DS_btn).click()

 #Assign pumps button
    AssignPmps_btn=(By.CSS_SELECTOR,'#lbEditDG')
    def Assignpmp(self):
        self.driver.find_element(*DG_Details.AssignPmps_btn).click()

    UnAssignPmp_btn=(By.CSS_SELECTOR,'#ctl00_ctl00_MasterPageContent_cpv_lbUnAssignPumps')
    def UnAssignpmp(self):
        self.driver.find_element(*DG_Details.UnAssignPmp_btn).click()


#------------------Locators of edit DG popup-----------------------
    #DGName
    DGName=(By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_dialogTxtDeploymentGroupName']")
    def edit_name(self,groupname):
        self.driver.find_element(*DG_Details.DGName).send_keys(groupname)
    def clear_DGName(self):
        self.driver.find_element(*DG_Details.DGName).clear()

    #DG description
    DG_Des=(By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_dialogTxtAreaDeploymentGroupDescription']")
    def edit_desc(self,grpdesc):
        self.driver.find_element(*DG_Details.DG_Des).send_keys(grpdesc)
    def clear_desc(self):
        self.driver.find_element(*DG_Details.DG_Des).clear()

    #DG DB
    DG_DB = (By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_cqiDatabaseDropDownList']")
    def DG_db(self,index):
        WebDriverWait(self.driver, 10)\
           .until(expected_conditions.visibility_of_element_located,((By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_cqiDatabaseDropDownList']")))
        DGDB_DDL = Select(self.driver.find_element(*DG_Details.DG_DB))
        print(len(DGDB_DDL.options))
        DGDB_DDL.select_by_index(index)
        sleep(3)
        self.driver.implicitly_wait(10)

#popup Save button
    Save_btn=(By.XPATH,"html/body/div[4]/div[3]/div/button[1]")
    def save_btn(self):
        self.driver.find_element(*DG_Details.Save_btn).click()
#popup cancel button
    cancel_btn=(By.XPATH,"html/body/div[4]/div[3]/div/button[2]")
    def Cancel(self):
        self.driver.find_element(*DG_Details.cancel_btn).click()
#--------------------locators of error messages-------------------
#locator of error message displayed when user enter duplicate DG name
    DG_Duplicatename=(By.XPATH, ".//*[@id='ctl00_ctl00_MasterPageContent_cpv_labelEditDGAlreadyUsedText']")
    def DuplicateDGname(self):
        Duplicate_error=self.driver.find_element(*DG_Details.DG_Duplicatename).text
        return Duplicate_error
#locator of error message when DG Name is deleted
    emptyname=(By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_labelDeploymentGroupNameRequired']")
    def empty_DG_name(self):
        empty_name_error=self.driver.find_element(*DG_Details.emptyname).text
        return empty_name_error

#locator of error message when DG description is deleted
    empty_desc=(By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_labelAreaDeploymentGroupDescriptionRequired']")
    def empty_DG_Des(self):
        empty_desc_error=self.driver.find_element(*DG_Details.empty_desc).text
        return empty_desc_error


#Assign Dataset popup
    Assign_DS_PWD=(By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_txtLoginPassword']")
    DS_Name=(By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_DropDownListDataSets']")
    DS_ID_Code=(By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_txtDSIDCode']")
    Assign_DS_confirm_btn=(By.XPATH,"html/body/div[4]/div[3]/div/button[1]")
    Assign_cancel_btn=(By.XPATH,"html/body/div[4]/div[3]/div/button[2]")

    def AssignDataset(self,pwd,name,ID):
        self.driver.find_element(*DG_Details.Assign_DS_PWD).send_keys(pwd)
        self.driver.find_element(*DG_Details.DS_Name).send_keys(name)
        self.driver.find_element(*DG_Details.DS_ID_Code).send_keys(ID)
        self.driver.find_element(*DG_Details.Assign_DS_confirm_btn).click()
        #Assign DS toast
    #DS_toast=(By.XPATH,"html/body/div[7]")
    DS_toast = (By.CSS_SELECTOR, 'html.firefox-42 body div.blockUI.toast.blockPage')


#Assign pump continue button
    Cont_btn=(By.XPATH,"html/body/div[4]/div[3]/div/button[1]")

    def cont_pmp_assign(self):
        self.driver.find_element(*DG_Details.Cont_btn).click()

    def Toast(self):
        toast_msg = self.driver.find_element(*DG_Details.DS_toast).text
        return toast_msg

#Screen appearance assertion
    def screen_displayed(self,how,what):
     try: self.driver.find_element(by=how,value=what)
     except NoSuchElementException as e:return False
     return True

#Assign Pump to DG
    # Browse_btn= (By.ID, 'ctl00_ctl00_MasterPageContent_cpv_ctlFileUpload')
    # Continue_btn = (By.XPATH, '/html/body/div[5]/div[3]/div/button[1]')
    # def Browse_File (self, Location):
    #     self.driver.implicitly_wait(20)
    #     self.driver.find_element(*DG_Details.Browse_btn).send_keys(Location)
    #     self.driver.find_element(*DG_Details.Continue_btn).click()