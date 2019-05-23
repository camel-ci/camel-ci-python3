import unittest
import random

from camel_bubblesort.bubblesort import randomTab
from camel_bubblesort.bubblesort import sortTab

class TestBubblesort(unittest.TestCase):

    def test_bubblesort(self):
        size = 10
        tab = randomTab(size)
        self.assertEqual(sortTab(tab),sorted(tab))
            
if __name__ == '__main__' :
    unittest.main()
