# map 2 voroodi migire . tabee,donbaale . 

#mesal tabdil celsious be fahrenheit


def celtofah (c):
   
    
    return (c * 9/5) + 32

#print(celtofah(30))

dama_ha = [0,2,4,8,12,21,23,30,40]

m = map(celtofah, dama_ha)

print(list(m))