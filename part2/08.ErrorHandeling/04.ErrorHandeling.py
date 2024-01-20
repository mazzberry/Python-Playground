


try: 
    f = open(r'C:\Users\Computer Center\Desktop\pythonFilePRC\b.txt')
   
    
    
except ModuleNotFoundError as e:
    print(e) 
    
else : 
        print(f.read())
        
finally:
    print('sar akhar man ejra misham .')
    f.close()