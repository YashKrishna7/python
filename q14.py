# employees={'Antony':55000,'Susan':45000,'Kiran':60000}
# a=dict(filter(lambda n:n[1]>=50000,employees.items()))
# b=dict(filter(lambda n:n[1]<50000,employees.items()))
# c={**{name:"high" for name in a},**{name:"low"for name in b}}
# print(c)
############another method###################################
employees={'Antony':55000,'Susan':45000,'Kiran':60000}
a=dict(map(lambda n:(n[0],'high'if n[1]>=50000 else 'low'),employees.items()))
print(a)