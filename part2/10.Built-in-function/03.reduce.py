#maxfinder proj

from functools import reduce


list1 = [1,45,21,44,32,65,12]

max_finder = lambda a,b : a if (a>b) else b

print(reduce(max_finder,list1))

