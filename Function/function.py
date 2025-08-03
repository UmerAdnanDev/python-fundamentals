#Function a reusable block of code
def hi():
    print("hi")
hi() #calling the function
def greeting(name): # name is parameter
    print(f"Greetings, {name} may you have a good day.")
greeting("Saim") #"Saim" is argument   
def welcome(name,place):
    print(f"Welcome {name} to {place}")
welcome("Karachi","Ahmed")
welcome(place="Lahore",name="Haseeb")
# welcome() will cause error as function is expection you to pass the arguments
def HBD(name ="",msg = "May you have many more!."):
    print(f"Happpy Birth Day to you {name}.\n{msg}")
HBD()
HBD(name ="Rayyan",msg = "May you live a happy life!.")
