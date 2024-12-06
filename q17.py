#with arguments and without return type
def add(num1,num2):
    sum=x+y
    print('Sum= ',sum)
def diff(num1,num2):
    difference=x-y
    print("Difference= ",difference)
def product(num1,num2):
    product=x*y
    print("Product= ",product)
def div(num1,num2):
    division=x/y
    print("Division=",division)
for i in range(5):
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("Enter the choice: "))
    if ch==1:
        x=float(input("Enter 1st number: "))
        y=float(input("Enter 2nd number: "))
        add(x,y)
    elif ch==2:
        x=float(input("Enter 1st number: "))
        y=float(input("Enter 2nd number: "))
        diff(x,y)
    elif ch==3:
        x=float(input("Enter 1st number: "))
        y=float(input("Enter 2nd number: "))
        product(x,y)
    elif ch==4:
        x=float(input("Enter 1st number: "))
        y=float(input("Enter 2nd number: "))
        if y!=0:
            div(x,y)
        else:
            print("Division by zero is not possible")
    elif ch==5:
        print("Exit")
        break
    else:
        print("Invalid input")