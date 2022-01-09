import unittest
import random
from sort import *

class sortTest(unittest.TestCase):

    def setUp(self):
        self.sortedL=[ i for i in range(100)]
        self.L=self.sortedL[:]
   
    def test_select_sort(self):
        select_sort(self.L)
        self.assertEqual(self.L,self.sortedL)
        
    def test_merge_sort(self):
        L1=merge_sort(self.L)
        self.assertEqual(L1,self.sortedL)     
   
if __name__ == '__main__':
    unittest.main()
