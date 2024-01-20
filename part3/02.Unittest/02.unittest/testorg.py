import unittest
import org

class test (unittest.TestCase):

    def test_sumon(self):
        self.assertEqual(org.sumon(10, 5) , 15 )
        self.assertEqual(org.sumon(-1, 1) , 0 )
        self.assertEqual(org.sumon(10, 10) , 20 )
        
    def test_divide(self):
        self.assertEqual(org.divide(6, 2),3)    
        self.assertEqual(org.divide(9, 3),3) 
        
        self.assertRaises(ValueError, org.divide , 10,0 )
        #or
        #with self.assertRaises(ValueError)
        #    org.divide(10,0)
        
    def test_multiply(self):
        self.assertEqual(org.multiply(2, 2),4)    
        self.assertEqual(org.multiply(2, 3),6) 
        
    def test_minus(self):
        self.assertEqual(org.minus(2, 2),0)    
        self.assertEqual(org.minus(2, 3),-1)         
    
    
    
if __name__ == "__main__":
    unittest.main()
