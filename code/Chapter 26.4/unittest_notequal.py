import unittest

class InequalityTest(unittest.TestCase):

    def testEqual(self):
        self.assertNotEqual(1, 3-2)

    def testNotEqual(self):
        self.assertEqual(2, 3-2)

if __name__ == '__main__':
    unittest.main()
