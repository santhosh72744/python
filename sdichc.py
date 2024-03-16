

#create a class pragati with a function welcome which displays the message welcome to pragati engineering college this pragati class should also display the details about departments and placements

class placements:
     def info(self):
         print("display we have 650 selected and still counting")
class dept:
    def display(self):
        print("cse")
        print("it")
        print("eee")
        print("ece")
        print("civil")
        print("ai")
class pragati (placements,dept):
    def welcome(self):
        print("welcome to pragati engineering college")
obj=pragati()
obj.welcome()
obj.info()
obj.display()
