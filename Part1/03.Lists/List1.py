

a = ['fizik' , 'riazi', 199555 , 140] 
b = ['a','b','cas','d']
c = [50,60,15,45]

a[2] = 2001 #avaz kardan yek slice dar list
del a[1] # pak kardan ozv
    
print(b + c)
print(b * 2)

print('varzesh' in a)


print(b[3])
print(a[2])
print(c[3])
print(a[0:3])


print(len(a))
print(max(b , key=len)) # darkhast mikonim bishtarin character too kodum string hast va neshun bede
print(min(b , key=len)) 
print(max(c))
print(min(c))

