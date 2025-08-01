#Variables:Containers that are used to hold data  (these are comments won't execute)
'''can contain alphanumeric characters and special characters
first character must be a variable or underscore _''' #multiline comments
""" name not equal to Name or NAME or any similar combination all are different
formats of writing : Snake case : _name_,name_is , Pascal case: Name,MyNameIs , Camel case: myName
can't use the name of special keywords or functions as names of variables"""
string = "Umer"
string_2 = 'Adnan'
string3 = '''Multi
            line 
            String'''
_text = """Multi
         line
         String"""
number = 12
decimal = 3.142
empty = None
boolean_1 = True
boolean_2 = False
complex = 2j
print(string) #dispaly value of variable on console through print() keyword
print(type(string)) #finding type of data
print(_text)
print(type(_text))
print(number)
print(type(number))
print(empty)
print(type(empty)) 
print(decimal)
print(type(decimal))
print(string)
print(type(string))
print(complex)
print(type(complex))
print("My age is"+str(number)) # can't concatinate string with other data types with other data types it will cause TypeError
print(f"My name is {string}")
print(1,string_2,3.5,True) #can't multi print without , will cause SyntaxError
#Outputs:

# Umer
# <class 'str'>  
# Multi
#          line  
#          String
# <class 'str'>
# 12
# <class 'int'>
# None
# <class 'NoneType'>
# 3.142
# <class 'float'>
# Umer
# <class 'str'>
# 2j
# <class 'complex'>
# My age is12
# My name is Umer
# 1 Adnan 3.5 True