

class person:
    
    
    def __init__(self , name):
        self.__name = name
        
    @property    
    def name(self):
        print('name getter')
        return self.__name
    
    
    @name.setter
    def name(self,Value):
        self.__name = Value
        print(f'setting name to {Value}')
        
        
    @name.deleter   
    def name (self):
        print('name deleter') 
        del self.__name  
        
        
a = person('Mohammad')
print(f'the name is {a.name}')    

a.name  = ('sara')
print(f'the name is {a.name}')


print(f'the name is {a.name}')


        
            