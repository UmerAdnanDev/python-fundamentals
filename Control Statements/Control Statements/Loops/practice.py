name = input("Enter your name: ")
courses = int(input(f"{name}, enter your number of courses: "))
nameofcourses = []
marksprcourse=[]
for i in range(courses):
    course = input(f"{i+1}) Enter name of Course: ")
    marks=float(input(f"{i+1}) Enter marks of {course} out of 50:"))
    nameofcourses.append(course)
    if marks>50:
       marks = 0
       marksprcourse.append(marks)
    else:
       marksprcourse.append(marks)
    # else:
    #     print("Invalid Input")
    #     if i == 0: i = -1
    #     else: i -=1
    #     continue
print(f"\t{name.title()}'s Mark Sheet")
total = 0
for i in range(courses):
    print(f"-{nameofcourses[i]}: {marksprcourse[i]}")
    total+=marksprcourse[i]
percentage = total/(courses*50) *100    
print(f"Percentage: {percentage}")