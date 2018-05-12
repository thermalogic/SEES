
import unittest

class Widget():
    def __init__(self, name,size = (40, 40)):
        self._name=name
        self._size=size

    def name(self):
        return self._name

    def size(self):
        return self._size

    def resize(self, width, height):
        if width < 0  or height < 0:
            raise ValueError("illegal size")
        self._size = (width, height)

    def dispose(self):
        pass

class DefaultWidgetSizeTestCase(unittest.TestCase):
    
    def test_default_widget_size1(self):
        widget = Widget('The widget1')
        
        self.assertEqual(widget.size(), (50, 50))
     
    def test_default_widget_size2(self):
        widget = Widget('The widget2')
        
        self.assertEqual(widget.size(), (40, 40))
        
    def test_default_widget_size3(self):
        widget = Widget('The widget3')
        self.assertRaises(ValueError, widget.resize,-1, 10)   
        
if __name__ == '__main__':
    unittest.main()        