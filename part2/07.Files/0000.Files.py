

with open(r'C:\Users\Computer Center\Desktop\pythonFilePRC\a.txt','r') as f:
    
    matn = f.read(15)
    print(matn , end=' ')
    
    f.seek(15)#***
    
    matn = f.read(15)
    print(matn , end=' ')
    
    