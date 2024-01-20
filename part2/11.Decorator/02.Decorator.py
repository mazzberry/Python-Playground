

def myDecorator(msg='message'):

    def Decorated(func):
        def wrapper(name):
            print('my decorator befor')
            print(f'payam daryafti : {msg}')
            func(name)
            print('my decorator after')

        return wrapper
    return Decorated


@myDecorator('in yek test ast')
def printname(name):
    print(name)


# printname = myDecorator(printname)

printname('Mohammad')
