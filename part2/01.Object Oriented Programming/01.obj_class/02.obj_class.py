
class empeloyee:
    def __init__(self , fname , lname , salary):
        self.fname = fname
        self.lname = lname
        self.email = fname +lname[0] + '@kevok.com'
        self.salary = salary




emp1 = empeloyee('Mohammad', 'Hosseini', '15000$')


print(emp1.email)

emp2 = empeloyee('Amir', 'behjat', '15000$')

print(emp2.email)
