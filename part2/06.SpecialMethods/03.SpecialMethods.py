

class book:
    
    def __init__(self, title , author , pages ):
        
        self.title = title
        self.author = author
        self.pages = pages
        print('Book has been created')
        
    def __str__(self):
        return "title: {} - author : {} - pages : {}".format(self.title,self.author,self.pages)
    
    def __len__(self):
        return self.pages  
    
    
        
a = book('Python', 'Eric Matthes' , 548)    

print(a)    
print(len(a))
        