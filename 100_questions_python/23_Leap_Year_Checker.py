n1=int(input("Enter the number : "));
if((n1%400==0)or(n1%4==0 and n1%100!=0)):
   print("Leap year");
else:
   print("Not a leap year");    