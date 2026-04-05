class Animal():
    def __init__(self,name ="",age = 0,eats ="",type = ""):
        self.name =name
        self.age = age
        self.eats = eats
        self.type = type
        if name!="":
         print(f"An Anime named {self.name} is created.") # will print as an object is initiated
        else:
           print("An Animal without any name is created.")
    def info(self):
       print("--Animal's Info--")
       print(f"- Name: {self.name}")
       print(f"- Age: {self.age} yr")
       print(f"- Diet: {self.eats}")
       print(f"- Type: {self.type}")
       print()
class Horned(Animal):
    def __init__(self,name ="",age = 0,eats ="",type = "",horn = 0):
       super().__init__(name,age,eats,type)
       self.horn = horn
       if horn > 0:
          print(f"I have {self.horn} horns.")
    def info(self):
       super().info()
       print(f"- Horns: {self.horn}")
class Insect(Animal):
   def __init__(self,name ="",age = 0,eats ="",type = "",legs = "",eyes =""):
       super().__init__(name,age,eats,type)
       self.legs = legs
       self.eyes = eyes
   def info(self):
      super().info()
      print(f"- legs: {self.legs}")
      print(f"- Eyes: {self.eyes}")
A1 = Animal("Sebas",3,"Dog food,Meat,Bones","carnivorous")
A1.info()
A2 = Horned("Shipu",2,"Grass,Hay,Fruits,Seeds ...etc","herbivorous",2)
A2.info()
A3 = Insect("Spidy",0.3,"bugs,flies,tiny insects","carnivorus",6,6)
A3.info()


      

