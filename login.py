def Login():
    print("Welcome To The Login Menu!")
    question1 = input("Please enter your username: ")
    if question1 == password1:
      question2 = input("Please enter your password: ")
      if question2 == password1:
         print("Details accepted")
        


def SignUp2():
    global password1
    password1 = input("Please enter a password you would like to use: ")
    question2 = input("Is " + password1 + " the correct password you would like to use: ")
    if question2 == "NO":
        SignUp2()
    if question2 == "YES":
        Login
    else:
        print("Incorrect response, please try again")
        SignUp2()


def SignUp1():
    global username1
    username1 = input("Please enter a username you would like to use: ")
    question1 = input("Is " + username1 + " the correct username you would like to use: ")
    if question1 == "NO":
        SignUp1()
    if question1 == "YES":
        SignUp2()
    else:
        print("Incorrect response, please try again")
        SignUp1()
        

def Login1():
    print("[Welcome to Pady's Password Manager!]")
    print("     Have you already signed up?")
    print("    Please Enter either YES or NO")
    print("--------------------------------------")
    Question1 = input("              : ")
    if Question1 == "NO":
        SignUp1()
    if Question1 == "YES":
        print("Login system!")

Login1()
