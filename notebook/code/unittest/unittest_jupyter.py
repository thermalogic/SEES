
import sys
import unittest

def run(*test_cases):
    for test_case in test_cases:
        suite = unittest.TestLoader().loadTestsFromTestCase(test_case)
        unittest.TextTestRunner(verbosity=1,stream=sys.stderr).run(suite)
