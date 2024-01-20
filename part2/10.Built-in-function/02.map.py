#masale map (ghabli ama ba lambda)

dama_ha = [0,2,4,8,12,21,23,30,40]


m = map(lambda c : (c * 9/5) + 32, dama_ha)

print(list(m))



a = [1,2,3]
b = [4,5,6]
c = [7,8,9]

d = map(lambda x,y,z: x+y+z , a,b,c)

print(list(d))