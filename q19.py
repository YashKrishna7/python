# with argument and with return type
def add(num1,num2):
    sum=x+y
    return sum
def diff(num1,num2):
    difference=x-y
    return difference
def product(num1,num2):
    product=x*y
    return product
def div(num1,num2):
    division=x/y
    return division
for i in range(5):
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("Enter the choice: "))
    if ch==1:
        x=float(input("Enter 1st number: "))
        y=float(input("Enter 2nd number: "))
        a=add(x,y)
        print(a)
    elif ch==2:
        x=float(input("Enter 1st number: "))
        y=float(input("Enter 2nd number: "))
        a=diff(x,y)
        print(a)
    elif ch==3:
        x=float(input("Enter 1st number: "))
        y=float(input("Enter 2nd number: "))
        a=product(x,y)
        print(a)
    elif ch==4:
        x=float(input("Enter 1st number: "))
        y=float(input("Enter 2nd number: "))
        if y!=0:
            a=div(x,y)
            print(a)
        else:
            print("Division by zero is not possible")
    elif ch==5:
        print("Exit")
        break
    else:
        print("Invalid input")