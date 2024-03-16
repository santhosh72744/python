#palindrom 1221  1221 check

n=int(input("enter the number"))
rev=0
temp=n
while(n>0):
    digit=n%10
    rev=rev*10+digit
    n=n//10
if(rev==n):
    print("yes palindrom")
else:
    print("no palindrom")
