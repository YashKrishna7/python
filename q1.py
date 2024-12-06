h=float(input("Enter the height: "))
w=float(input("Enter the weight: "))
def bmi(h,w):
    a=h/100
    b=a**2
    z=w/b
    return(z)
x=bmi(h,w)
print("BMI is",x ,"kg/m^2")