

class karmand:
    
    raise_amt = 1.05
    
    
    def __init__(self, name , lname , salary):
        self.name = name
        self.lname = lname
        self.salary = salary
        
        
    @property
    def email(self):
        return '{}{}@Kevok.com'.format(self.name,self.lname)
    
    @property
    def fullname (self):
        return '{} {}'.format(self.name , self.lname)
    
    def applyraise (self):
        self.salary = (self.salary * self.raise_amt)
        
    
    
    

        
        
        