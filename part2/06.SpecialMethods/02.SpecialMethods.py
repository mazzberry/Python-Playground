

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
    #################################################################################specialmethod
    def __repr__(self):
       return f"developer ('{self.fname}'-'{self.lname}'- {self.salary})"#.format(self.fname,self.lname,self.salary)   
    #################################################################################specialmethod
       
class Manager(empeloyee):
    def __init__(self , fname , lname , salary , emps = None):# emps = None yani bdadn gharare 
        #moteghayer hayi ro daryaft konim (muteable things mest list va dict)
        super().__init__(fname, lname, salary)
        if emps is None:
            self.emps = []
        else:
            self.emps = emps    
            
    def add_emp(self , emp):# add kardan emp be zir majooe manager
        if emp not in self.emps: 
            self.emps.append(emp)
    
    def remove_emp(self , emp):# pak kardan emp az zir majmooe manager
        if emp in self.emps:
            self.emps.remove(emp)
    
    def print_emp (self):
        for emp in self.emps:
            print('===>' , emp.fullName())            
            



emp1 = empeloyee('ali', 'molae', 25000) 
dev1 = developer('Mohammadreza', 'Hosseini', 28000 , 'Python')
dev2 = developer('sara', 'saree', 18000 , 'sql')
mgr1 = Manager('Mahdi', 'Behjati', 25000 )


print(dev1)
print(dev2)