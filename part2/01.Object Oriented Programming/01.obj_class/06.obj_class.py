
class empeloyee:
    
    raise_amt = 1.04
    num_of_emp = 0
    
    def __init__(self , fname , lname , salary):#hardafe ba nam borda class hadaghal 1 bar ejra mishe
        self.fname = fname
        self.lname = lname
        self.email = fname +lname[0] + '@kevok.com'
        self.salary = salary
        empeloyee.num_of_emp +=1 #shemordan dafaat estefade
    
    def fullName(self):
        
        return f'{self.fname} {self.lname}'
    
    def applyRaise(self):
        self.salary = int(self.salary *  self.raise_amt)
        
        
        
emp1 = empeloyee('ali', 'karimi', 23000)   
emp2 = empeloyee('Mohammadreza', 'Hosseini', 25000) 
emp3 = empeloyee('reza', 'shokufe', 20000)   

emp1.raiseAmt = 1.06
emp1.applyRaise()
print(emp1.salary)
emp2.applyRaise()
print(emp2.salary)
print(empeloyee.num_of_emp)
  

#print(empeloyee.__dict__)
#print(emp1.__dict__)