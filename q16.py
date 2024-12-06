#without argument and without return type
x=float(input("Enter 1st number: "))
y=float(input("Enter 2nd number: "))
def add():
    sum=x+y
    print('Sum= ',sum)
def diff():
    difference=x-y
    print("Difference= ",difference)
def product():
    product=x*y
    print("Product= ",product)
def div():
    division=x/y
    print("Division=",division)
for i in range(5):
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("Enter the choice: "))
    if ch==1:
        add()
    elif ch==2:
        diff()
    elif ch==3:
        product()
    elif ch==4:

        if y!=0:
            div()
        else:
            print("Division by zero is not possible")
    elif ch==5:
        print("Exit")
        break
    else:
        print("Invalid input")