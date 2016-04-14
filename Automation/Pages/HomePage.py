from selenium.webdriver.common.by import By
#Test

class HomePage():
    LoginName_LBL = (By.CSS_SELECTOR,'span#ctl00_globalNavigation_logonNameLogo b')


    def get_login_name(self):
        lable = self.driver.find_element(*HomePage.LoginName_LBL).text
        return lable

