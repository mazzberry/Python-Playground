# __iter__ qabel khana mikone.
# __next__ be badi mire.


list1 = [1,2,3,4,5]

my_Iter = iter(list1)


while True:
    try:
        element = next(my_Iter)
        print(element)
        
    except StopIteration:
        break   
    

    
        
        
        
    


