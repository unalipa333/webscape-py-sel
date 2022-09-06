
#inheritance and multiple inheritance
#polymorphism


class Dogs:
    


    def __init__(self,breed, name,age,level,color):
        self.name=name
        self.age=age
        self.level=level
        self.color=color
        self.breed=breed

    def __str__(self):
            
            return  f"{self.name, self.age, self.breed, self.color, self.level, self.color }"

    def bark(self):
        if self.age < 2:
            return "woof!"

        elif self.age < 7:
            return "WOOF!"

        else:
            return "meow"



class Golden(Dogs):
    def __init__(self,breed, name,age,level,color):
        super().__init__(breed, name,age,level,color)



class Rotty(Dogs):
    def __init__(self,breed, name,age,level,color):
        super().__init__(breed, name,age,level,color)

    def bark(self):
        if self.age < 2:
            return "ruff!"

        elif self.age < 7:
            return "RUFF!"

        else:
            return "I'm a cat"

poky= Rotty("rot","poky", 1, "jr", "black")
print(poky.__str__())
print(poky.bark())



class Pit(Dogs): 
    def __init__(self,breed, name,age,level,color):
        super().__init__(breed, name,age,level,color)



class PitRott(Pit, Dogs):
    def __init__(self,breed, name,age,level,color):
        super().__init__(breed, name,age,level,color)


pup=PitRott("pitrot","pup", 99, "jr", "black")
print(pup.bark())
print(pup)