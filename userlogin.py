from userlogin import *
class order:
    print("existing user or new user")
    t=int(input())
    obj=landr()
    if t==1:
        n=input()
        p=input()
        e=input()
        obj.regis(n,p,e)
        print("registration successful")
    elif t==2:
        n=input()
        p=input()
        if obj.userlogin(n,p):
            print("userlogin successful")
        else:
            print("wrong details try again")