from animal import Animal

class Dog(Animal):
    def __init__(self, eats, sounds):
        super().__init__(eats,sounds)

    #def food(self):
        #print(self.name + " eats")  

    def sound(self):
        return self.sounds

    def eat(self):
       return self.eats


dog_1 = Dog(" "," ")
#dog_1.food()
print(dog_1.eat())
print(dog_1.sound())
