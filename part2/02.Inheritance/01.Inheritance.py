
class empeloyee:
    raiseamt = 1.04
    num_of_emp = 0
    
    def __init__(self , fname , lname , salary):
        self.fname = fname
        self.lname = lname
        self.email = fname +lname[0] + '@kevok.com'
        self.salary = salary
        empeloyee.num_of_emp +=1
    
    def fullName(self):
        
        return f'{self.fname} {self.lname}'
    
    def applyRaise(self):
        self.salary = int(self.salary *  self.raiseamt)

class developer(empeloyee):
   raiseamt = 1.06 # class attribut tavanayi taqir dar baghie class hay inharited ro dare #jaleb
   def __init__(self , fname , lname , salary , language):
       super().__init__(fname, lname, salary) # zakhire sazi az class ers borde shode
       #va niaz be zakhire sazi dobare nist
       self.language = language
     


dev1 = empeloyee('Mohammadreza', 'Hosseini', 25000) 
dev2 = developer('Mohammadreza', 'Hosseini', 28000 , 'Python')

print(dev1.fullName())
print(dev2.fullName())
dev2.applyRaise()
print(dev2.salary)
