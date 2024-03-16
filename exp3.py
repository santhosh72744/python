def login():
    while True:
        username=input("enter your username")
        password=input("enyer your password")
        if username == password:
            print("login successfully")
            break
        else:
            print("you have entered wrong credentials")
login()
