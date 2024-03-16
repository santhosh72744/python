import csv
class landr:
    def registration(self,username,password,phnno,pincode,city):
        self.uname=usernameself
        self.pwd=password
        self.phnno=phoneno
        self.pin=pincodeself
        self.city=city
        with open("student.csv","a",newline"") as file:
           store=csv.writer(file)
           store.writerow([self.uname,self.pwd,self.phnno,self.pin,self.city])
    def login(self,username,password):
         with open("student.csv","r",newline="") as file:
              read=csv.dictreader(file)
             for row in read:
                if row["uname"]=username and row["pwd"]=password:
                    return True
         return false