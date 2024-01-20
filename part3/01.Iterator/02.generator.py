

def mygen():
    n=1
    print('this is first')
    yield n
    
    n+=1
    print('this is second')
    yield n
    
    n+=1
    print('this is last')
    yield n
    
    
a = mygen()
    
print(next(a))
print(next(a))
print(next(a))