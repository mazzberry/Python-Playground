

class Car:
    def __init__(self , speed , color):
        self.__speed = speed # ba 2 underscore capsule sazi roosh anjam shod, dar zakhire sazi
        self.__color = color
    
    def set_speed(self,value):    
        self.__speed = value 
    
    def get_speed(self): 
        
        return self.__speed
        
        



peykan = Car(100, 'white')


peykan.set_speed(110)
peykan.__speed = 130

print(peykan.get_speed())
