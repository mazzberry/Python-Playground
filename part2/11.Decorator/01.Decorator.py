

def myDecorator(func):
    def wrapper():
        print('my decorator befor')
        func()
        print('my decorator after')

    return wrapper


def printname():
    print('Mohammadreza hosseini')


printname = myDecorator(printname)

printname()

# ________________________________hamchenin_____________________________________________
print('HAMINTOR________')


def myDecorator(func):

    def wrapper(name):##(*args) or (*args , **kargs)
        print('my decorator befor')
        func(name)##(*args) or (*args , **kargs)
        print('my decorator after')

    return wrapper


@myDecorator
def printname(name):# or (*args) or (*args , **kargs)
    print(name)# or (*args) or (*args , **kargs)
    

# printname = myDecorator(printname)


printname('Mohammadreza')
