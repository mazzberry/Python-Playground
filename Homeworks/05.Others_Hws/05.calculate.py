

def calculator():
    '''
    ###
    mashin hesab
    ###
    '''
    operation = input('''
                     choose one opration : 
                     + :
                     - :
                     * :
                     / :
                     
                     ''')
    
    num1 = int(input('Enter the first number :'))
    num2 = int(input('Enter the second number :'))
    
    if operation == '+':
        print(num1+num2)
        
    elif operation == '-':
        print(num1-num2)    
        
    elif operation == '*':
        print(num1*num2)
        
    elif operation == '/':
        print(num1/num2)
    
    else :
        print('operation ra dorost entekhab nakardid!!!')    
        
    again()    
        
        
        
def again():
    '''
    ###
    donbale calclulate
    ###
    '''
    calcAgain = input('''
    aya mikhahid edame daahid  :
    baray edame : Y
    va
    baray khoruj : N
    
    ''')       
        
    if calcAgain.upper() == 'Y':
        calculator()
    elif calcAgain.upper() == 'N':
        print('kharej shodid')  
        pass
    else :
        again()  
        
calculator()        
    
        
    