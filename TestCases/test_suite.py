import unittest
import os
import sys
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TestCases.test_Login import LoginTest
from TestCases.test_CreateUsers import test_users
from TestCases.test_CreateRole import Roles
from TestCases.test_Role_Edit import Roles_Edit
from TestCases.test_Delete_Role import Roles_Delete

from TestCases.test_DG_Valid_create import test_DG_Create
from TestCases.test_DG_invalid_creation import test_invalid_create
from TestCases.test_DG_Valid_Edit import DG_validEdit
from TestCases.test_DG_Invalid_Edit import DG_InvalidEdit
from TestCases.test_DG_AssignPumps import AssignPumps
from TestCases.test_DG_deletePmps import
from TestCases.test_DG_AssignDS import Assign_DS
from TestCases.test_DG_Delete import test_DGDelete




from Reporting_Lib import HTMLTestRunner
import xmlrunner


login_suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
users_suite = unittest.TestLoader().loadTestsFromTestCase(test_users)
Roles_suite = unittest.TestLoader().loadTestsFromTestCase(Roles,Roles_Edit,Roles_Delete)
Datasets_suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
DeploymentGroup_suite = unittest.TestLoader().loadTestsFromTestCase(test_DG_Create,test_invalid_create,DG_validEdit,DG_InvalidEdit,AssignPumps,Assign_DS,test_DGDelete,test_DG_deletepmps)
Pumps = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

smoke_test = unittest.TestSuite([login_suite,users_suite,Datasets_suite,DeploymentGroup_suite,Pumps])

outfile = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\Report" + time.strftime("%Y%m%d-%H%M%S") + ".html", "w")
print (outfile.name)
#create Test Report
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title= 'test', description = 'Smoke test report')
print ("Runner prepared ..")
# runner = xmlrunner.XMLTestRunner(output="test-results")
runner.run(smoke_test)
print ("Runner Done ..")

if __name__ == "main":
    unittest.main()






