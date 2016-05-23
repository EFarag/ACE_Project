import unittest
from selenium import webdriver
from ddt import data,unpack
from DataSource.read_excel import read_excel
import os.path

class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        Weblink = self.get_URL(self)
        self.driver.get(Weblink)
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        self.driver.close()




    def get_URL(self):

      URL = read_excel.get_data_from_excel(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)) +  '\Data\Test_Data.xlsx' ,'Weblink')
      return URL[0]


if __name__ == '__main__':
    unittest.main()
