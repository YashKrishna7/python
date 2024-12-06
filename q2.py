s={1,2,3,4,5,6}
print("s=",s)
lst=list(s)
lst.remove(5)
lst.insert(4,1)
x=set(lst)
print("After adding one, the set is ",x)