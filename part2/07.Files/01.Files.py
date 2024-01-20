# 1
# ++++behine nist++++
with open(r'C:\Users\Computer Center\Desktop\pythonFilePRC\a.txt') as rf:
    print(
        'behine nist'
    )
    matn = rf.read()
    print(
        matn
    )


print('_________________________')


# ++++behine hast.++++
with open(r'C:\Users\Computer Center\Desktop\pythonFilePRC\a.txt') as f:
    print(
        'be soorat behine.'
    )
    for matn in f:                   # proce loading ro barash tarif kardim...
        print(
            matn, end=' '
        )
