class Student:
    def __init__(self,name = "No-Name",age = 0 ,grades = "X"):
        self.name = name
        self.age = age
        self.grades = grades
S1 = Student("Faik",17,"A-")
print(f"S1 -> Name: {S1.name} , Age: {S1.age} , Grade: {S1.grades}")
S2 = Student()
print(f"S2 -> Name: {S2.name} , Age: {S2.age} , Grade: {S2.grades}")
