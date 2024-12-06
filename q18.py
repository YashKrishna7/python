#without argument and with return type
x=float(input("Enter 1st number: "))
y=float(input("Enter 2nd number: "))
def add():
    sum=x+y
    return sum
def diff():
    difference=x-y
    return difference
def product():
    product=x*y
    return product
def div():
    division=x/y
    return division
for i in range(5):
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("Enter the choice: "))
    if ch==1:
        a=add()
        print(a)
    elif ch==2:
        a=diff()
        print(a)
    elif ch==3:
        a=product()
        print(a)
    elif ch==4:
        if y!=0:
            a=div()
            print(a)
        else:
            print("Division by zero is not possible")
    elif ch==5:
        print("Exit")
        break
    else:
        print("Invalid input")