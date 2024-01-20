#barname in benvisid dar html tag ra begirad va bebandad va matn ra vasast qarar dahahd

def httags(tag , word):
    return '<%c><%s></%c>' %(tag , word , tag)



print (httags('b'  , 'salam ostad '))
    


