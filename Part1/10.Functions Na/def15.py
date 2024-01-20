

def calc_factorial(x):
    '''factorial function'''
    if x == 1:
        return 1
    else:
        return (x * calc_factorial(x-1))
    
    
print(calc_factorial(3))
    
