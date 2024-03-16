class faculty:
    def __init__(self,f_name,dpartment,f_id):
        self.f_name=f_name
        self.dpartment=dpartment
        self.f_id=f_id
    def print_info(self):
        print("faculty information=",self.f_name,self.dpartment,self.f_id)
obj=faculty("santhosh","it",1243)
obj.print_info()

class cse(faculty):
    pass
obj=cse("jyostna mam","computer_science",1234)
obj.print_info()
