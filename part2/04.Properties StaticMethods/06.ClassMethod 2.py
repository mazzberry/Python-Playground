
from datetime import date


class Person:
    
    
    def __init__(self , name , age):
        self.name = name
        self.age = age
    
    @classmethod #dar zaman estefade kardan az cls dar (def) neveshtan @classmethod vajebe
    def yearConverter(cls , name , Year):
        return cls(name,(date.today().year - Year))
    # cls az stuff save shode dar __init__(class) 
    #ro ejaze seda zada neshun ro tooye yek function dige mide
    
        
        
        
            
        
    def display(self):
        print(f'my name is {self.name} and i have {self.age} old')  
        
        
      
a = Person('Mohammadreza', 19)

a1 = Person.yearConverter('Mohammadreza', 2004)

a1.display()
a.display()