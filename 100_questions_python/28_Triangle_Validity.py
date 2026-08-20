n1=int(input("Enter the first side : "));
n2=int(input("Enter the second side : "));
n3=int(input("Enter the third side : "));
if(n1+n2>n3 and n2+n3>n1 and n1+n3>n2):
    print("It is a triangle ");
else:
    print("It is not a triangle")