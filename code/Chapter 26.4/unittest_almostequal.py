import unittest

class AlmostEqualTest(unittest.TestCase):

    def testNotAlmostEqual(self):
        self.assertNotAlmostEqual(1.1, 3.3-2.0, places=1)

    def testAlmostEqual(self):
        self.assertAlmostEqual(1.1, 3.3-2.0, places=0)

    def testAlmostEqualWithDefault(self):
        self.assertAlmostEqual(1.1, 3.3-2.0)

if __name__ == '__main__':
    unittest.main()
