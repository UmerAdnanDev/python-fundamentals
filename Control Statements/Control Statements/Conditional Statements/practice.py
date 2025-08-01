#Simple Calculator
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
print("Operators")
print("-Addition: +")
print("Subtraction: -")
print("Multiplication: x")
print("Division: /")
print("Exponential: ^")
op = input("Enter Operator:")
if op == "+":
    print(f"The sum of {num1} & {num2}: {num1+num2}")
elif op == "-":
    print(f"The difference of {num1} & {num2}: {num1-num2}")
elif op == "x":
    print(f"The Product of {num1} & {num2}: {num1*num2}")
elif op == "/":
    print(f"The Division of {num1} & {num2}: {num1/num2}")
elif op == "^":
    print(f"The Power of {num1} by {num2}: {num1**num2}")                
else:
    print("Invalid Input")    