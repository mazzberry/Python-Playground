

class Animal:
    
    
    def __init__(self):
        print('animal class created')
    
    def whoami(self):
        print('i am animal')
        
    def eat(self):
        print('i am eating')          
        
    
#a = Animal()




class dog(Animal):
    species = 'mammal'# class attribute

    def __init__(self): # khaz = ture yani yek jay khali 
        #ba variable pishfarz
        super().__init__()
        print('class of dog created')
        
    def whoami(self):
        print('i am Dog') 
        
    def eat(self):
        print('i am eating')  
    
    def wagh():
        print('wagh wagh')       
        
        
        
b = dog()        
           
b.whoami()           
    
        
        
        
        
