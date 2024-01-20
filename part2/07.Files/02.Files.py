#2
#mafhoom seek : 


with open (r'C:\Users\Computer Center\Desktop\pythonFilePRC\a.txt') as f:
    matn = f.read(15)
    print(
        matn , end = ' '
    )
    
    f.seek(16)
    
    matn = f.read(15)
    
    print(
        matn , end=' '
    )
