import unittest

class AlmostEqualTest(unittest.TestCase):

    def test_NotAlmostEqual(self):
        self.assertNotAlmostEqual(1.11, 1.3, places=1)

    def test_AlmostEqual(self):
        self.assertAlmostEqual(1.1, 1.3, places=0)

    def test_AlmostEqualWithDEfault(self):
        self.assertNotAlmostEqual(1.1, 1.3)

if __name__ == '__main__':
    unittest.main()