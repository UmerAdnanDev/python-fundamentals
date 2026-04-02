#Constructor is usedto pass a value to a Class
class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
P1 = Person("Daniel",18,"Male")
print(f"- Name: {P1.name}")
print(f"- Age: {P1.age}")
print(f"- Gender: {P1.gender}")
#default,parameterized,with default values