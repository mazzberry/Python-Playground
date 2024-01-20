#tabei benvisid ke chek konad key darkhasti dar dic vojud dard yakheyr

car = {'brand': 'chevrolet','model': 'corvet', 'year':'1965','country': 'usa'}

def isKeyPeresent(vari):
    ''' key checker '''
    if vari in car:
        print ('that key u want is available')
    else:
        print('zereshk')
    
    return vari    
    


print(isKeyPeresent('brand'))