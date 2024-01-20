

#4
with open(r'C:\Users\Computer Center\Desktop\pythonFilePRC\a.txt','r') as rf:
    
    with open(r'C:\Users\Computer Center\Desktop\pythonFilePRC\b.b.txt','w') as wf:
        for Line in rf:
            wf.write(
                Line
            )