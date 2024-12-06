####list comprehension#######
# l=[1,2,3,4,5]
# a=list(map(lambda n:n*2,l))
# print(dict(zip(l,a)))


#dictionary comprehension


keys=['a','b','c']
values=[1,2,3]
dict_values={k:v for (k,v) in zip(keys,values)}
print(dict_values)