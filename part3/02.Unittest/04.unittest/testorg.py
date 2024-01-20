import unittest
from org import karmand

class test_karmand(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setUp class')
    
    @classmethod
    def tearDownClass(cls):
        print('tearDownclass')    
    
    
    
    
    
    #baray inke nemune sazi tekrari tooye har function nadashte bashim az method (setUp) estefade mikonim 
    #va nemune pishfarz ro behesh midim ...
    
    def setUp(self):
        print('setUp')
        self.emp_1 = karmand( 'Mohammad', 'Hosseini', 34000)
        self.emp_2 = karmand( 'ali', 'jahromi', 16000)
        
    def tearDown(self): # pas az anjam shodan test va gereftan result mitunim ba in method
        #dasturati bedim (mesl : pas az anjam shodan test etelaat ro az database pak kon)
        print('Teardown\n')    
        
        
        # yademun nare ke bayad posht har nemune dar function self ro estefade konim ta shenakhte beshe.
        
    
    
    def test_email(self):
        print('email.test')
       
        
        self.assertEqual(self.emp_1.email , 'MohammadHosseini@Kevok.com')
        self.assertEqual(self.emp_2.email , 'alijahromi@Kevok.com')
        
        
        
        
    def test_fullname(self):
        print('fullname.test')
       
        self.assertEqual(self.emp_1.fullname , 'Mohammad Hosseini' )
        
        
    def test_applyraise(self):
        print('applyraise.test')
        
        
        self.emp_1.applyraise()
        self.emp_2.applyraise()
        
        self.assertEqual(self.emp_1.salary, 35700)
        self.assertEqual(self.emp_2.salary, 16800)
            
        
        
        
if __name__ == '__main__':
    unittest.main()        