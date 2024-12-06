x=float(input("Enter 1st number: "))
y=float(input("Enter 2nd number: "))
for i in range(5):
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit")
    ch=int(input("Enter the choice: "))
    if ch==1:
        sum=x+y
        print("Sum= ",sum)
    elif ch==2:
        difference=x-y
        print("Difference = ",difference)
    elif ch==3:
        product=x*y
        print("Product = ",product)
    elif ch==4:
        if y!=0:
            division=x/y
            print("Division = ",division)
        else:
            raise Exception("Division by zero is not possible")
    elif ch==5:
        print("Exit")
        break
    else:
        print("Invalid input")
