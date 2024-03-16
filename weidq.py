#create a class ticket which will be the abstract class inside that create a function book ticket which will be the abstract method as nothing in it
#create a class make my trip which will use the book ticket function from ticket class to take the details such as name,phn num,email id,journey date and displays a message saying thank you form make  y trip
#create a class IRCTC which uses the book ticket of ticket class and takes the same details as make my trip but in the end it will given option to the user to selcet whether it is one way or round trip
#if the user option is round trip it  again asks the user to enter the return date as well and prints the message from thank you irctc else it prints the message thank you for choosing irctc
#create a class indigo which takes all the details as irctc and just asks which mood of transport you want to going train,flight or bus and displays thank you for choosing indigo

from abc import ABC,abstractmethod
class ticket((ABC):
             
             
    @abstractmethod
    def bookticket(self)
    pass
class makemytrip(ticket):
    def bookticket(self):
        print(self,enter name,phnnum,journey_date):
        print("enter name",self.name)
        print("enter name",self.phnnum)
        print("enter name",self.email)
        print("enter name",self.journey_date)
        print("thank you for booking from makemytrip")
obj=makemytrip()
obj.ticket("santhosh",9966945626,"santhosh.72744@gmail.com",15)
class irctc(ticket):
