n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
print("Before swap",n1,"and",n2);
n1,n2=n2,n1;
print("After sway",n1,"and",n2);

n1=n1+n2;
n2=n1-n2;
n1=n1-n2;
print("After swap",n1,"and",n2);