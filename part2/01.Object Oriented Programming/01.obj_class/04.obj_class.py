

class dog:
    species = 'mammal'# class attribute

    def __init__(self , breed , name , khaz  = True ): # khaz = ture yani yek jay khali 
        #ba variable pishfarz
        self.name = name
        self.khaz = khaz
        self.breed = breed
        
        
        
frank = dog('bulldog','frank', khaz=False) # =False pishfarz ro taghir dadim       

print (frank.breed)
print(frank.khaz)

