# raise keyword is used to create a custom exception in python
try:
 age = int(input("Enter your age to access this site: "))
 if age <= 18:
    raise Exception("Your are too young to access this site.")
 elif age > 100 or age < 1:
    raise Exception("Enter your actual age.")
except Exception as msg:
   print(f"Error Message: {msg}")



