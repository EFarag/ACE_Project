import os
import time
import unittest
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from TestCases.test_Login import LoginTest
from TestCases.test_CreateUsers import test_users
from TestCases.test_CreateRole import Roles
from TestCases.test_Role_Edit import Roles_Edit
from TestCases.test_Delete_Role import Roles_Delete
from TestCases.test_ImportDataSet import Datasets
from TestCases.test_DeleteDS import Delete_Dataset
from TestCases.test_DG_Valid_create import test_DG_Create
from TestCases.test_DG_invalid_creation import test_invalid_create
from TestCases.test_DG_Valid_Edit import DG_validEdit
from TestCases.test_DG_Invalid_Edit import DG_InvalidEdit
from TestCases.test_DG_AssignPumps import AssignPumps
#from TestCases.test_DG_deletePmps import
from TestCases.test_DG_AssignDS import Assign_DS
from TestCases.test_DG_Delete import test_DGDelete
# from TestCases.test_Pumps import test_Pumps
from TestCases.test_DGSave_cont import test_DG_Creation
from Reporting_Lib import HTMLTestRunner



login_suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
users_suite = unittest.TestLoader().loadTestsFromTestCase(test_users)
Roles_Creation_suite = unittest.TestLoader().loadTestsFromTestCase(Roles)
Role_Edit_suite =unittest.TestLoader().loadTestsFromTestCase(Roles_Edit)
Role_Delete_suite =unittest.TestLoader().loadTestsFromTestCase(Roles_Delete)
Datasets_Creation_suite = unittest.TestLoader().loadTestsFromTestCase(Datasets)
Datasets_Delete_suite = unittest.TestLoader().loadTestsFromTestCase(Delete_Dataset)
DeploymentGroup_ValidCreate_suite = unittest.TestLoader().loadTestsFromTestCase(test_DG_Create)
DeploymentGroup_InvalidCreate_suite = unittest.TestLoader().loadTestsFromTestCase(test_invalid_create)
DeploymentGroup_ValidEdit_suite = unittest.TestLoader().loadTestsFromTestCase(DG_validEdit)
DeploymentGroup_InvalidEdit_suite = unittest.TestLoader().loadTestsFromTestCase(DG_InvalidEdit)
DeploymentGroup_Save_suite = unittest.TestLoader().loadTestsFromTestCase(test_DG_Creation)
DeploymentGroup_AssignDS_suite = unittest.TestLoader().loadTestsFromTestCase(Assign_DS)
DeploymentGroup_AssignPumps_suite = unittest.TestLoader().loadTestsFromTestCase(AssignPumps)
DeploymentGroup_Delete_suite = unittest.TestLoader().loadTestsFromTestCase(test_DGDelete)
# Pumps_suite = unittest.TestLoader().loadTestsFromTestCase(test_Pumps)

smoke_test = unittest.TestSuite([login_suite,users_suite,Roles_Creation_suite,Role_Edit_suite,Role_Delete_suite,Datasets_Creation_suite,Datasets_Delete_suite,DeploymentGroup_ValidCreate_suite,DeploymentGroup_InvalidCreate_suite,DeploymentGroup_ValidEdit_suite,DeploymentGroup_InvalidEdit_suite,DeploymentGroup_Save_suite,DeploymentGroup_AssignDS_suite,DeploymentGroup_AssignPumps_suite,DeploymentGroup_Delete_suite])


outfile = open(os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + "\Report_" + time.strftime("%Y%m%d-%H%M%S ") + ".html", "w")
print (outfile.name)
#create Test Report
runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title= 'ACE Execution Status', description = 'Smoke test report')
print ("Runner prepared ..")
runner.run(smoke_test)
print ("Runner Done ..")

if __name__ == "main":
    unittest.main()
