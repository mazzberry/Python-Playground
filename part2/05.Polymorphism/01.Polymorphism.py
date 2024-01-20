#polimorphism = chand rikhti

class shark:
    
    def swim(self):
        print('shark is swiming now')
        
    def swimBackward(self):
        print('shark cant swim on backward')    
        
    def sharkSkeleton(self):
        print('shark has a big skeleton')    
        

class clownfish:
    
    def swim(self):
        print('clownfish is swiming now')
        
    def swimBackward(self):
        print('clownfish can swim b')    
        
    def clownfishSkeleton(self):
        print('clownfish has a small skeleton')  


def inTheOcean(fish):
    fish.swimBackward()        
    
    
sammy = shark()
jimi = clownfish()
jack = shark()


inTheOcean(jimi)



