import unittest
from tests import (test_auth,
                   test_auth_endpoint,
                   test_snails_endpoint,
                   test_races_endpoint,
                   test_single_snail_endpoint,
                   test_rounds_endpoint,
                   test_single_race_endpoint,
                   test_single_round_endpoint,
                   test_results_endpoint,
                   test_single_result_endpoint,
                   test_command_create_user)
import xmlrunner
import sys

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(test_auth))
suite.addTests(loader.loadTestsFromModule(test_snails_endpoint))
suite.addTests(loader.loadTestsFromModule(test_races_endpoint))
suite.addTests(loader.loadTestsFromModule(test_auth_endpoint))
suite.addTests(loader.loadTestsFromModule(test_results_endpoint))
suite.addTests(loader.loadTestsFromModule(test_single_race_endpoint))
suite.addTests(loader.loadTestsFromModule(test_single_snail_endpoint))
suite.addTest(loader.loadTestsFromModule(test_rounds_endpoint))
suite.addTest(loader.loadTestsFromModule(test_single_round_endpoint))
suite.addTest(loader.loadTestsFromModule(test_single_result_endpoint))
suite.addTest(loader.loadTestsFromModule(test_command_create_user))


# initialize a runner, pass it your suite and run it
runner = xmlrunner.XMLTestRunner(verbosity=3, output='test-reports/unittest')

ret = not runner.run(suite).wasSuccessful()
sys.exit(ret)
