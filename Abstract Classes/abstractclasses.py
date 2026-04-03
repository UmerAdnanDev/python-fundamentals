from abc import ABC,abstractmethod # from abc module importing ABC base class and abstractmethod keyword
class Bird(ABC):#abstract classes can't initiate an object
    @abstractmethod
    def eats(self): #abstract method needs to be implemented by the child class
        pass
    def fly(self,name = "Bird"):
        print(f"{name} can fly")
class Pigeon(Bird):
    def eats(self):
        print("Pigeon eats seeds")
p1 = Pigeon()
p1.eats()
p1.fly("Pigeon")
print("Abstract classes can't have objects")
# b1 = Bird() TypeError: Can't instantiate abstract class Bird without an implementation for abstract method 'eats'
# b1.fly()
#the abstract method must be implemented by the child class