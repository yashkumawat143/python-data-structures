n1=int(input("Enter the number : "))

rev=0
while(n1>0):
    digit=n1%10;
    rev=rev*10+digit;
    n1=n1//10;
print(rev)