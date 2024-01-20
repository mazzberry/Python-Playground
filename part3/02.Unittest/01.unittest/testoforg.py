import unittest

import orgcodets


class testcalc(unittest.TestCase):
    
    def test_add(self):
        result = orgcodets.sumon(2,2)
        self.assertEqual(result, 4)
        
if __name__=='__main__':
    unittest.main()  
      