
import unittest

class EqualityTest(unittest.TestCase):

    def test_Equal(self):
        self.assertEqual(3, 3)

    def test_NotEqual(self):
        self.assertNotEqual(2, 5-2)   

class AlmostEqualTest(unittest.TestCase):

    def testAlmostEqual(self):
        self.assertAlmostEqual(1.12, 1.11, places=1)

    def testNotAlmostEqual(self):
        self.assertNotAlmostEqual(1.12, 1.21, places=1)
        
def suiteEqual():
    suite = unittest.TestSuite()
    suite.addTest(EqualityTest('test_Equal'))
    suite.addTest(AlmostEqualTest('assertAlmostEqual'))
    return suite

def suiteNotEqual():
    suite = unittest.TestSuite()
    suite.addTest(AlmostEqualTest('testNotAlmostEqual'))
    return suite

if __name__ == '__main__':
    #unittest.main(defaultTest = 'suite2')
    unittest.main(defaultTest = 'suiteEqual')
  