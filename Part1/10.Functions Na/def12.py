

## *args = (3,'ali') tuple hast
## *Kwargs = {'name':'ali' , 'job':'engineer;}

def personinfo(*args, **kwargs):
    print(args)
    print(kwargs)
    
    


userInfo_1 = ['software dev','single']
userInfo_2 = {'name':'Mohammad', 'degree':'diploma','goals':'be a nice person in front of god'}

personinfo(*userInfo_1 , **userInfo_2)