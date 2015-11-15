import unittest
from widget import Widget

class WidgetTestCase(unittest.TestCase):

    def setUp(self):
        self.widget = Widget('The widget')

    def tearDown(self):
        self.widget.dispose()

    def test_default_size(self):
        self.assertEqual(self.widget.size(), (50,50),
                         'incorrect default size')
    def test_resize(self):
        self.widget.resize(100,150)
        self.assertEqual(self.widget.size(), (100,150),
                         'wrong size after resize')

def suite():
    suite = unittest.TestSuite()
#    suite.addTest(WidgetTestCase('test_default_size'))
    suite.addTest(WidgetTestCase('test_resize'))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest = 'suite')

#    runner = unittest.TextTestRunner()
#    runner.run(suite())
    
