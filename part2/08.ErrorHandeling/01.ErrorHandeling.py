

try:
    f = open(r'C:\Users\Computer Center\Desktop\pythonFilePRC\b234.txt')
    import safad

except FileNotFoundError:
    print(' file peyda nashod')

except ModuleNotFoundError:
    print('module mored nazar vojud nadarad')
