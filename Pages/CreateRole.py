import selenium
from selenium.webdriver.common.by import By

class RolesPage():
    Roles_BTN = (By.LINK_TEXT,'Roles')

    def Roles (self):
      self.driver.find_element(*RolesPage.Roles_BTN).click()