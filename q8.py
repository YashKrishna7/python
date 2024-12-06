name=input("Enter the Username: ")
x=name.isalnum()
y=len(name)
if x==True or 6<=y<=15:
    print("Username is valid")