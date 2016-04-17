import selenium
from selenium.webdriver.common.by import By


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
    self.drive.implicitly_wait(30)


class Upload():
 fileUpload =(By.XPATH,'/html/body/div[6]/div[2]/div[1]/input')
 SubmitButton = (By.XPATH,"/html/body/div[6]/div[3]/div/button[1]")

 def File_Upload(self,location):
  self.driver.find_element(*Upload.fileUpload).send_keys('C:/VP Only 4DE7.mgr')
  self.driver.find_element(*Upload.SubmitButton).click()


