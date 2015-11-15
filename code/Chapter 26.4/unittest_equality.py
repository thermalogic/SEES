import unittest

class EqualityTest(unittest.TestCase):

    def testEqual(self):
        self.assertEqual(1, 3-2)

    def testNotEqual(self):
        self.assertNotEqual(2, 3-2)

if __name__ == '__main__':
    unittest.main()
