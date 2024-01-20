

class Car:
    def __init__(self , speed , color):
        self.speed = speed 
        self.color = color
    
    def set_speed(self,value):    
        self.speed = value 
    
    def get_speed(self): 
        
        return self.speed
        
        



peykan = Car(100, 'white')
peride = Car(120, 'black')

peykan.set_speed(110)
peykan.speed = 130 #***

print(peykan.get_speed())



