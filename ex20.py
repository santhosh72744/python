n=int(input("enter the number"))
mod=0
n1=n
while(n>0):
    mod=mod+1
    n=n//10
sod=0
digit=n1
while(n1>0):
    digit=n1%10
    sod=sod+digit**mod
    n1=n1//10
if(sod==mod):
    print("yes")
