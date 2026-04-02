class Avatar():
    def fields(self,name,hp,atk,element,lvl):
        self.name = name
        self.health = hp
        self.attack = atk
        self.element = element
        self.level = lvl
    def info(self):
         print("---Avatar's Info---")
         print(f"- Name: {self.name}")
         print(f"- Level: {self.level}")
         print(f"- Health: {self.health}")
         print(f"- Attack: {self.attack}")
         print(f"- Element: {self.element}")
    def Attack(self):
       print(f"{self.name} used {self.element} infused attack with {self.attack} damage.")
chr1 = Avatar()
chr1.fields("Chrollo",450,154,"Darkness",6)
chr1.info()
chr1.Attack()
chr2 = Avatar()
chr2.fields("Freecs",510,198,"Dragonic",7)
chr2.info()
chr2.Attack()
#testing
print(chr1.name)