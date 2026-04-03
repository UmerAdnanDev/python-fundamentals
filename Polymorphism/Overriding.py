class Animal():
    def eats(self):
        print("Animal eats food")
    def drinks(self):
        print("Animal drinks water")
class Cow(Animal): #inheritence
    def eats(self):
        print("Cow eats grass")
class Cat(Animal):
    def eats(self):
        print("Cat eats fish")
    def drinks(self):
        print("Cat drinks milk")        
A1 = Animal()
A2 = Cow()
A3 = Cat()
A1.eats()
A1.drinks()
print()
A2.eats()
A2.drinks()
print()
A3.eats()
A3.drinks()
print()

                           