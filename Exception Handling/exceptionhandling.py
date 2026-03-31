try:
    zero = 0
    num = 12 / 0 # leads to infinity causes ZeroDivisionError
except(ZeroDivisionError):
    print("Can't Divide A Number by Zero")
finally:
    print("finally block will run either way") #  isn't a mandatory block
print()
try:
    string = "string"
    num = 12 + string
except(TypeError):
    print("These Data Types don't support this operation")
print()
try:
    string = "string"
    num = 12 / string
except(TypeError):
    print("These Data Types don't support this operation")
print()
try:
    list_ = [1,2,3]
    print(list_[3])
except(IndexError):
    print("Index can't be accesssed")
print()
try:
    n = 1/0 + "x" 
except(Exception): # works for all
    print("There is an Exception Raised")
print()
try:
    string = "string"
    num = 12 / string
except Exception as e:
    print(f"Exception Message: {e}") #give the exact reason why error was caused
print()