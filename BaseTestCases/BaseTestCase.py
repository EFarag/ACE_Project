import unittest
from selenium import webdriver


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://10.1.23.215/AGW")
        self.driver.maximize_window()

    @classmethod
    def tearDown(self):
        self.driver.close()



if __name__ == '__main__':
    unittest.main()
