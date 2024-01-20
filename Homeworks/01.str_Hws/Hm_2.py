# barname in benvisid ba voroodi 3 adad gerefte shode az karbar
# moratabeshun kone


x = int(input('adad aval : '))
y = int(input('adad dovom : '))
z = int(input('adad sevom : '))


a1 = min(x,y,z)
a2 = max(x,y,z)
a3 = (x + y + z) - a1 - a2

print(f'numbers sorted : {a1,a3,a2}')
