class Error(Exception):
    pass

class theImportedValueIsLowerThandNmber(Error):
    pass

class theImportedValueIsHigherThanNumber(Error):
    pass





number = 23 

while True:
    
    try:
        u_input = int(input('adad ra vared konid : '))
        
        if u_input < number:
            raise theImportedValueIsLowerThandNmber()
        
        elif u_input > number:
            raise theImportedValueIsHigherThanNumber()
        
        break

    except theImportedValueIsLowerThandNmber:
        print("adad kuchak tar az  adad mazmun ast")
    except theImportedValueIsHigherThanNumber:
        print("adad bozorgtar az  adad mazmun ast")
        
print('adad dorost ast')        
        
