# classi benvisid ke mohit o masahat dayere ra bedast biarad


class hendese:
    
    def __init__(self , r):
        self.radius = r
    
    def circle_env(self):
        
        return f'masahat barabar ast ba : ',( self.radius * 2 ) * 3.14
    
    def circle_area(self):
        
        return f'mohit barabar ast ba : ',(self.radius**2)*3.14
    
test = hendese(8) 
print(test.circle_area())
print(test.circle_env())

        
        
    