class Parent():
    def whosmethod(self):
        print("Parent Method")
class Child(Parent):
    def whosmethod(self):
        super().whosmethod() # uses parents implementation
        print("Now Overridden by child")
p1 = Parent()
p1.whosmethod()
print()
c1 = Child()
c1.whosmethod() 
