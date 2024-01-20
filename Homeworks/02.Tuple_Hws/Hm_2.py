# aazayi ra be tuple ezafe konid

tup1 = (1,2,5,4,6,7)
print(tup1)

tup1 = tup1 + (9,)
print(tup1)


#ezafe kardan mian aza

tup1 = tup1[:2] + (45,85,66) + tup1[:2]
print(tup1)

#

listx = list(tup1)
listx.append(99)

print(listx)