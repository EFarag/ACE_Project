import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class Dataset():
   Datasetink = (By.LINK_TEXT,'Data Sets')

   def Dataset_link(self):
    self.driver.find_element(*Dataset.Datasetink).click()


class Dataset_import():
  Import_button= (By.ID,'ctl00_ctl00_MasterPageContent_cpv_lblBtnImport')


  def Import(self):
    self.driver.find_element(*Dataset_import.Import_button).click()


class Import_Password():
  dataset_password = (By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtActionPassword')
  dataset_submit = (By.CSS_SELECTOR,'body > div:nth-child(6) > div.ui-dialog-buttonpane.ui-widget-content.ui-helper-clearfix > div > button:nth-child(1)')

  def Password(self,password):
    self.driver.find_element(*Import_Password.dataset_password).send_keys('P@ssw0rd')
    self.driver.find_element(*Import_Password.dataset_submit).click()
    #self.driver.implicitly_wait(20)


class Upload():
 fileUpload =(By.XPATH,'/html/body/div[6]/div[2]/div[1]/input')
 SubmitButton = (By.XPATH,'/html/body/div[6]/div[3]/div/button[1]')

 def File_Upload(self,location):
   self.driver.implicitly_wait(20)
   self.driver.find_element(*Upload.fileUpload).send_keys(location)
   self.driver.find_element(*Upload.SubmitButton).click()


class ID_code():
 ID_Code_TXT =(By.ID,'ctl00_ctl00_MasterPageContent_cpv_txtImportDSCode')
 Import_Button = (By.XPATH,'/html/body/div[3]/div[3]/div/button[1]')

 def Dataset_Import(self,IDC):
   self.driver.find_element(*ID_code.ID_Code_TXT).send_keys(IDC)
   self.driver.find_element(*ID_code.Import_Button).click()
   self.driver.implicitly_wait(30)