
try:
    f = open(r'C:\Users\Computer Center\Desktop\pythonFilePRC\b.txt')
    import safad

except (FileNotFoundError, ModuleNotFoundError):
    print(' file peyda nashod ya module vojud nadarad')

# except ModuleNotFoundError:
   # print ('module mored nazar vojud nadarad')

finally:
    print('man sar akhar ejra mishavanm...')
    f.close()