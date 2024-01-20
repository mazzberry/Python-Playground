

class Karmand:
    
    raise_amt = 1.04
    num_of_emp = 0
    
    def __init__(self, name, lname, pay):
        self.name = name
        self.lname = lname
        self.pay = pay
        self.email = name  + '@kevok.com'
        Karmand.num_of_emp += 1 
        
    def nameGetter(self):
        return f'{self.name} {self.lname}'  

    def ramt (self):
        self.pay = int(self.pay * self.raise_amt)
        
    
    
emp1 = Karmand('Mohammad','Hosseini', 5000) 
emp2 = Karmand('Moh','Hossein', 50) 
emp3 = Karmand('ahmad','Hos', 5) 
   

 

print(emp1.pay)
emp1.ramt()
print(emp1.pay)
print(Karmand.num_of_emp)