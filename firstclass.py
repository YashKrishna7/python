def upper_fun(fun):
    def inner_fun(name):
        result=fun(name)
        return result.upper()
    return inner_fun
@upper_fun
def hello_Name(name):
    return "hello " + name
# f=upper_fun(hello_Name)
# print(f('navarang')) #print(upper_fun(hello_Name('navarang)))
print(hello_Name('navarang'))
# 
# def good_morning(name):
#     return "good Morning "+ name
# print(upper_fun(hello_Name,'Yash'))
# print(upper_fun(good_morning,'Yash'))

# 