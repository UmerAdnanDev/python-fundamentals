#Local variables: variables defined with in a function which can only be accessed in the function
#Global variables: variable defined outside the function which can be access any where even in function
a = 2
def function(a):
    return a 
print(f"Local Variable: {function(1)}") #a = 1
print(f"Global Variable: {a}")#a =2
