#! /usr/bin/python

import unittest
from US5testcases import DispenseNow

# get all tests from US5-test
dispense_now = unittest.TestLoader().loadTestsFromTestCase(DispenseNow)

# create a test suite
test_suite = unittest.TestSuite(dispense_now)

# run the suite
unittest.TextTestRunner(verbosity=2).run(test_suite)
