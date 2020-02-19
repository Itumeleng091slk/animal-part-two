from animal import Animal

class Dog(Animal):
    def __init__(self, eats, sounds):
        super().__init__(eats,sounds)

    #def food(self):
        #print(self.name + " eats")  

    def sound(self):
        return self.sounds,"Bark"

    def eat(self):
       return '{0} food'.format(self.eats)


dog_1 = Dog(" "," ")
#dog_1.food()
dog_1.eat()
dog_1.sound()