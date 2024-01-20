#append shodan


num_list = [x for x in range(20) if x % 2 == 0]

print(num_list)

#another exp

num_list2 = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list2)

#another exp

num_list3 = ['even' if i % 2 == 0 else 'odd' for i in range(0,10)]

print(num_list3)