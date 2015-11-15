import unittest

class TruthTest(unittest.TestCase):

    def test_AssertTrue(self):
        self.assertTrue(True)

    def test_AssertFalse(self):
        self.assertFalse(False)

if __name__ == '__main__':
    unittest.main()
