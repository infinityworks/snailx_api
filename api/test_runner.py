import unittest
from tests import test_main, test_auth, test_auth_endpoint, test_snails_endpoint, test_races_endpoint
import xmlrunner
import sys

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_main))
suite.addTests(loader.loadTestsFromModule(test_auth))
suite.addTests(loader.loadTestsFromModule(test_snails_endpoint))
suite.addTests(loader.loadTestsFromModule(test_races_endpoint))
suite.addTests(loader.loadTestsFromModule(test_auth_endpoint))

# initialize a runner, pass it your suite and run it
# runner = unittest.TextTestRunner(verbosity=3)
runner = xmlrunner.XMLTestRunner(verbosity=3, output='test-reports/unittest')

ret = not runner.run(suite).wasSuccessful()
sys.exit(ret)
