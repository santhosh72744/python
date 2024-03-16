#check whether if the number is divisible by its sum of digits or not
a=int(input("enter a number"))
n=12345
sum=0
while(n>0):
    digit=n%10
    sum=sum+digit
    n=n//10
if(sum%a==0):
    print("divisible")
else:
    print("not divisible")
