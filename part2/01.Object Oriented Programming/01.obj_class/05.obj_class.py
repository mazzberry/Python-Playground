#Class attribute
class empeloyee:
    
    raiseAmt = 1.04 #class attribute
    
    
    def __init__(self , fname , lname , salary):
        self.fname = fname
        self.lname = lname
        self.email = fname +lname[0] + '@kevok.com'
        self.salary = salary
    
    def fullName(self):
        
        return f'{self.fname} {self.lname}'
    
    def applyRaise(self):
        self.salary = int(self.salary *  self.raiseAmt)
        
        
        
emp1 = empeloyee('ali', 'karimi', 23000)   
emp2 = empeloyee('Mohammadreza', 'Hosseini', 25000) 
emp3 = empeloyee('reza', 'shokufe', 20000)   

  
  
print(empeloyee.raiseAmt)
print(emp1.raiseAmt)
print(emp2.raiseAmt)