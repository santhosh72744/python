import csv
class landr:
    def registration(self,username,password,phnno,pincode,city)
    self.uname=username
    self.pwd=password
    self.phnno=phoneno
    self.pin=pincodeself
    self.city=city

    with open("student.csv","a",newline="")as file:
        store=csv.writer(file)
        store.writer([self.uname,self.pwd,self.phnno,self.pin.self.city])
        