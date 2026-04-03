class Parent(): #parent / super class
    def __init__(self,name ="noname",age = 0):
        self.name = name
        self.age = age
    def Name(self): # methods can't use the field names in naming
        if self.name =="noname" or self.name == None:
            print("I don't have a name.")
        else:
            print(f"My name is {self.name}.")
    def Age(self):
        if self.age > 0:
            print(f"My age is {self.age}.")
        else:
            print("I don't know my age.")        
class Child1(Parent): #child / sub class which inherited from parent class
    def Child(self):
        print("I am a Child Class")
p1 = Parent()
p1.Name()
p1.Age()
print()
c1 = Child1("James",12)
c1.Name()
c1.Age()
c1.Child()
print()
c2 = Child1()
c2.Name()
c2.Age()
c2.Child()
#The child class can use the attributes of parent and also it's own attributes