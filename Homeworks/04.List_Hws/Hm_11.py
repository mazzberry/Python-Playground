# remove kon adaad doublecate ro az list

a = [1,1,2,440,2,3,3,440,4,50,50]

dupItems = set()
unicItems = []

for x in a:
    if x not in dupItems:
        unicItems.append(x)
        dupItems.add(x)
        
print(dupItems)        
