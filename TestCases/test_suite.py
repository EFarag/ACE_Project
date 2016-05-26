import unittest
from TestCases.test_Login import LoginTest
from Reporting_Lib import HTMLTestRunner


login_suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
smoke_test = unittest.TestSuite([login_suite])

outfile = open("D:\Report.html", "w")
#create Test Report
runner = HTMLTestRunner.HTMLTestRunner(
            stream=outfile,
            title= 'test',
            description = 'smoke test suite report'
        )
runner.run(smoke_test)










