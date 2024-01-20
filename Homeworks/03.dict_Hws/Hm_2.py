

a = {'brand': 'chevrolet','model': 'corvet', 'year':'1965','country': 'usa'}


def deleter(key):
    global a
    for i in a:
       if key in a:
           del a[f'{key}']
           
           print(f'{key} hazv shod')
           
           return i
           
    
    else:   
       print('key vojud nadarad')
        
        
print(deleter('year'))  

print(a)
    
        