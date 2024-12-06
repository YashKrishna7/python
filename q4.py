String="Hello world from Python"
lst=list(String)
lst.reverse()
print("Reverse of String is ",lst)
result=list(dict.fromkeys(lst))
print("String after removing duplicates: ",result)
letter_count={}
for char in result:
    letter_count[char]=letter_count.get(char,0) + 1
print("Letter counts:",letter_count)
