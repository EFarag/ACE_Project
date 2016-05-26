import unittest
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TestCases.test_Login import LoginTest
from Reporting_Lib import HTMLTestRunner
import xmlrunner


login_suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
smoke_test = unittest.TestSuite([login_suite])

outfile = open("Report.html", "w")
#create Test Report
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title= 'test', description = 'smoke test suite report')

# runner = xmlrunner.XMLTestRunner(output="test-results")
runner.run(smoke_test)








