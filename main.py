import csv
class landr:
    def userlogin(self,u,p):
        with open("userinfo.csv","r",newline="")as file:
            read=csv.DictReader(file)
            for row in read:
                if row['username']==u and row['password']==p:
                    return True
            return False
    def registration(self,username,password,email):
        self.uname=username
        self.pwd=password
        self.em=email
        with open('userinfo.csv','a',newline="") as file:
            a=csv.writer(file)
            a.writerow([self.uname,self.pwd,self.em])