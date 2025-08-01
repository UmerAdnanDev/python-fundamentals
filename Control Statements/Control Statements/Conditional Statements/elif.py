#Multi line if-else-elif statement
print("Marks per subject are 50")
name = input("Enter your name: ")
name = name.title()
s1 = int(input("Enter the marks of 1st subjects: "))
s2 = int(input("Enter the marks of 2nd subjects: "))
s3 = int(input("Enter the marks of 3rd subjects: "))
s4 = int(input("Enter the marks of 4th subjects: "))
total = s1+s2+s3+s4
percentage = total / 200 *100
if(percentage >=90 and percentage<=100):
    print(f"{name} you got {total} out of 200.\n Your percentage is {percentage}.\n Your Grade is A+") 
elif(percentage >=80):
    print(f"{name} you got {total} out of 200.\n Your percentage is {percentage}.\n Your Grade is A") 
elif(percentage >=70):
    print(f"{name} you got {total} out of 200.\n Your percentage is {percentage}.\n Your Grade is B") 
elif(percentage >=60):
    print(f"{name} you got {total} out of 200.\n Your percentage is {percentage}.\n Your Grade is C")
elif(percentage >=50):
    print(f"{name} you got {total} out of 200.\n Your percentage is {percentage}.\n Your Grade is D") 
else:    
    print(f"{name} you got {total} out of 200.\n Your percentage is {percentage}.\n Your Grade is F .\n You Failed")
