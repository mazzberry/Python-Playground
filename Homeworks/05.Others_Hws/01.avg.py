#barname ie bennvisid average listi ra be dast biarad

n= int(input('tedad dars hara vared konid : '))
a = []

for i in range(0,n):
    e= float(input(f'nomre dars {i+1} : '))
    a.append(e)


avg = (sum(a)/n)


print('the avg is :' , (round(avg,2)))

