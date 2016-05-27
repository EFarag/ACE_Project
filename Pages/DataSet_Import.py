from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class Dataset():
    #DataSet Locators
    Datasetink = (By.LINK_TEXT,'Data Sets')
    DS_label = (By.ID,'ctl00_ctl00_MasterPageContent_breadCrumbs_uxBreadcrumbSiteMap_ctl04_uxBreadcrumbLabel')
    Import_button= (By.ID,'ctl00_ctl00_MasterPageContent_cpv_lblBtnImport')
    dataset_password = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtActionPassword')
    dataset_submit = (By.CSS_SELECTOR,'body > div:nth-child(6) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1)')
    fileUpload =(By.XPATH,'/html/body/div[6]/div[2]/div[1]/input')
    SubmitButton = (By.XPATH,'/html/body/div[6]/div[3]/div/button[1]')
    ID_Code_TXT =(By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtImportDSCode')
    Delete_Code_ID =(By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtDataSetId')
    Import_Button = (By.XPATH,'/html/body/div[3]/div[3]/div/button[1]')
    Submit_Delete= (By.XPATH,'html/body/div[6]/div[3]/div/button[1]')
    Toast_Label =(By.XPATH,'html/body/div[7]')
    invalid_label =(By.ID,'ctl00_ctl00_MasterPageContent_cpv_labelRegexValidatorFileUpload')
    Required_Label =(By.ID,'ctl00_ctl00_MasterPageContent_cpv_labelRequiredFieldValidatorFileUpload')
    Delete_BTN =(By.ID,'ctl00_ctl00_MasterPageContent_cpv_lblBtnDelete')
    Delete_Password = (By.XPATH,".//*[@id='ctl00_ctl00_MasterPageContent_cpv_txtActionPassword']")
    Delete_Toast_Msg =(By.XPATH,'html/body/div[9]')
    DSGrid = (By.XPATH, ".//*[@id='ctl00_ctl00_MasterPageContent_cpv_lstDatasets_itemPlaceholderContainer']/tbody/tr")

    Page_elements = (Datasetink,DS_label,Import_button,dataset_password,dataset_submit,fileUpload,SubmitButton,ID_Code_TXT,Import_Button)

    #DataSet Methods

    #Method to click on the dataset link on Home page
    def Dataset_link(self):
        self.driver.find_element(*Dataset.Datasetink).click()

    #Method to Assert that dataset link is redirecting successfully to Dataset page
    def DS_Assert(self):
        DS_Label = self.driver.find_element(*Dataset.DS_label).text
        return DS_Label

     #Method to click on the Import Button
    def Import(self):
        self.driver.find_element(*Dataset.Import_button).click()

    #Method to insert the Dataset password
    def Password(self,password):
        self.driver.find_element(*Dataset.dataset_password).send_keys('P@ssw0rd')
        self.driver.find_element(*Dataset.dataset_submit).click()

    #Method to upload the dataset file, giving the location of file
    def File_Upload(self,location):
        self.driver.implicitly_wait(20)
        self.driver.find_element(*Dataset.fileUpload).send_keys(location)
        self.driver.find_element(*Dataset.SubmitButton).click()

    #Method to insert the dataset ID code, IDC is the code that got from DDT
    def Dataset_Import(self,IDC):
       self.driver.find_element(*Dataset.ID_Code_TXT).send_keys(IDC)
       self.driver.find_element(*Dataset.Import_Button).click()
       self.driver.implicitly_wait(10)

    #Method to check the Toast message that confirm the uploading of Dataset file
    def Toast_Message(self):
        self.driver.implicitly_wait(3)
        Label_TXT = self.driver.find_element(*Dataset.Toast_Label).text
        return Label_TXT

    def Invalid_file(self):
       Label_TXT = self.driver.find_element(*Dataset.invalid_label).text
       return Label_TXT


    def Required_filename(self):
       Label_TXT = self.driver.find_element(*Dataset.Required_Label).text
       return Label_TXT

#****************************************Delete Dataset******************************


    def Delete_DataSet(self, DS_name):
        options_List = []
        options_List = self.driver.find_elements(*Dataset.DSGrid)
        options_List.pop(0)
        for option in options_List:
            DSname = option.find_element(By.XPATH, ".//td[1]").text
            if DSname == DS_name:
                CB = option.find_element(By.XPATH, ".//td[1]/span")
                CB.click()
                self.driver.find_element(*Dataset.Delete_BTN).click()
                break
    def Dataset_Delete_code(self,IDC):
       self.driver.find_element(*Dataset.Delete_Code_ID).send_keys(IDC)
       self.driver.find_element(*Dataset.Submit_Delete).click()
       self.driver.implicitly_wait(10)

    def Delete_Toast(self):
        Label_TXT = self.driver.find_element(*Dataset.Delete_Toast_Msg).text
        return Label_TXT



class Popup_Assertion():
    def is_element_present(self,how,what):
        try: self.driver.find_element(by=how,value=what)
        except NoSuchElementException as e:return False
        return True
