import unittest
import sys
import HtmlTestRunner
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Scripts.test_emailtransfer import MailTransferTest

dirpath = os.getcwd()


class TestRun:

    tc_1 = unittest.TestLoader().loadTestsFromTestCase(MailTransferTest)

    adhocTestSuite = unittest.TestSuite([tc_1])
    unittest.TextTestRunner(adhocTestSuite)


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=dirpath+"/../Reports/"))
