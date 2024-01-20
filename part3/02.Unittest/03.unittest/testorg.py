import unittest
from org import karmand

class test_karmand(unittest.TestCase):
    
    
    def test_email(self):
        emp_1 = karmand( 'Mohammad', 'Hosseini', 34000)
        emp_2 = karmand( 'ali', 'jahromi', 16000)
        
        self.assertEqual(emp_1.email , 'MohammadHosseini@Kevok.com')
        self.assertEqual(emp_2.email , 'alijahromi@Kevok.com')
        
        emp_1.name = 'hasan'
        
        self.assertEqual(emp_1.email , 'hasanHosseini@Kevok.com')
        
        
    def test_fullname(self):
        emp_1 = karmand( 'Mohammad', 'Hosseini', 34000)
        emp_2 = karmand( 'ali', 'jahromi', 16000)
        self.assertEqual(emp_1.fullname , 'Mohammad Hosseini' )
        
    def test_applyraise(self):
        emp_1 = karmand( 'Mohammad', 'Hosseini', 34000)
        emp_2 = karmand( 'ali', 'jahromi', 16000)    
        
        emp_1.applyraise()
        emp_2.applyraise()
        
        self.assertEqual(emp_1.salary, 35700)
        self.assertEqual(emp_2.salary, 16800)
            
        
        
        
if __name__ == '__main__':
    unittest.main()        