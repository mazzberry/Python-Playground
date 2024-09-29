

for i in range(1,11):
    for j in range(1,11):
        k =  i * j
        print(k ,end=' ')
    print()    

#List Comprehension 
 
x = [(k, str(k)) for k in range(50)]
x = [k for k in range(50)]
print(x) 