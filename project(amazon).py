#create an ecommerce project where the user can register and login itself we can see what all products are accepts contain name,price,category,stock left from these products 
#user can replace the product just by the product and quantity he wants to purchase once he enter this a bill should be generated with the total amountand the mesage should be given order as been place complete the payment on the delivery 
#the change of the stock sholud be reflected on the total product list 

import csv
class student():
    def studentdetails
f=open("student.csv","a",newline="")
a=csv.writer(f)
a.writerow(["studentid","rollnum","name","mobilenum"])
studentid=int(input("enter student id:"))
rollnum=int(input("enter your rollnum",))
name=input("enter your name")
mobilenum=int(input("enter your mobilenum"))
a.writerow([studentid,rollnum,name,mobilenum])
print("student record has save")