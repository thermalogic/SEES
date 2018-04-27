import unittest

class AlmostEqualTest(unittest.TestCase):

    def test_NotAlmostEqual(self):
        self.assertNotAlmostEqual(1.11, 3.3-2.0, places=1)

    def test_AlmostEqual(self):
        self.assertAlmostEqual(1.1, 3.3-2.0, places=0)

    def test_AlmostEqualWithDEfault(self):
        self.assertNotAlmostEqual(1.1, 3.3-2.0)

if __name__ == '__main__':
    unittest.main()