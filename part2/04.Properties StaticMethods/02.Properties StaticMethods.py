

class pop_artist:
    
    
    
    def __init__(self , name):
        self.__name = name
        
        
    @property   
    def name(self):
        return self.__name
    
    
    @name.setter
    def name(self,value):
        self.__name = value
        print(f'name changed to {self.__name}')
    
    @name.deleter    
    def name(self):
        print('esm mored nazar pak shod')
        del self.__name 
        
        
        
        
n1 = pop_artist('khosravi')
n2 = pop_artist('jonny cash')
n3 = pop_artist('judas the priest')
n3 = pop_artist('metalica')

print(n1.name)

n1.name = ('Ahmadvand')

print(n1.name)

print(n3.name)

del n3.name

