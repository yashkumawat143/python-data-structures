

a=int(input("Enter the amount : "));
p=int(input("Enter the starting money : "));
r=int(input("Annul interest rate : "));
n=int(input("Enter the insert amount : "));
t=int(input("Time in year : "));
a=p*(1+r/n)**n*t;
print(a);