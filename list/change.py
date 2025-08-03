#List is mutable & dynamic meaninf it can be altered and new item can be added
Fruits = ["Apple","Mango","Banana","Strawberry"]
         #   0       1        2          3
Fruits[2] = "Kiwi" #changing one item
print(Fruits)
# Fruits[4] = "Cherry" can't access an index which doesn't exist
Fruits[0:3] = "Coconut","Blueberry","Rasberry" #changing multiple items
print(Fruits)
