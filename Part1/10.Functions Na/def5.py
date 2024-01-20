#vared kardan variable global dar function


a = 3
def add_1():
    global a
    a = a + 2
    
    return a


print(add_1())


# variable hay local dar function


def add_2():
    
    b = 2
    b = b + 5
    
    return b

print(add_2())

    