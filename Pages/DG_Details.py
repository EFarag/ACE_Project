import selenium
from selenium.webdriver.common.by import By
from time import sleep

class DG_details():
    DG_Checkbox=(By.ID,'checkboxImage52667099758332')
    AssignDs_btn=(By.ID,'buttonUpdateDS')
    AssignPmp_btn=(By.ID,'lbEditDG')
    ContinuePmp_btn=(By.XPATH,'/html/body/div[5]/div[3]/div/button[1]')

    def DG_screenlink (self):
        self.driver.find_element(*DG_details.DG_screen).click()
        self.driver.find_element(*DG_details.AssignDs_btn).click()
        self.driver.find_element(*DG_details.AssignPmp_btn)
        self.driver.find_element(*DG_details.ContinuePmp_btn)
