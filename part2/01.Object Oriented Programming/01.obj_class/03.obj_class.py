


class empeloyee:
    def __init__(self , fname , lname , salary):
        self.fname = fname
        self.lname = lname
        self.email = fname +lname[0] + '@kevok.com'
        self.salary = salary
    
    def fullName(self):
        
        return f'{self.fname} {self.lname}'



emp1 = empeloyee('mohammad', 'hosseini', 15000)

print(emp1.fullName().title())
