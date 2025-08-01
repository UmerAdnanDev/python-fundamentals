#Double line If-else statement
guests = ["Hasseb","Ali","Hammad","Kareem"]
name = input("Enter your name: ")
# title make string in this form Title
n = name.title()
if(n in guests):
    print(f"{n} you are allowed to enter in the party.")
else:
    print(f"{n} you are not allowed to enter in the party.")    