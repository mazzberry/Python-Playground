

## *args = (3,'ali') tuple hast
## *Kwargs = {'name':'ali' , 'job':'engineer;}

def personinfo(*args, **kwargs):
    print(args)
    print(kwargs)
    
    
personinfo('software dev','single',name = 'Mohammad' , age = 19) 
