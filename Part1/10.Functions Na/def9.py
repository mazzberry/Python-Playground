
# baray error nadan : vared nakardan variable hay tabee(func) pishfarza hayi mizarim
# greet = Hi nemoone pishfarz

def sayHello(name = 'yourname' , greet = 'Hi' ):
    '''first enter the name.
    then select type of greet toward language '''
    return f'{greet} {name}'


print(sayHello())