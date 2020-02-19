class Animal:
    def __init__(self, eats,sounds):
        #self.name = name
        self.sounds = sounds
        self.eats = eats

    #def food(self):
        #print("{0} eats".format(self.name))

    def sound(self):
        #print("bark")
       # return '{0} '.format(self.sounds)
       return self.sounds
    
    def eat(self):
        #print("food")
       # return '{0} 'return self.sounds.format(self.eats)
        return self.eats
        
dog = Animal(" food ", " Bark")
cat =Animal(" ", "meow") 
#print(dog.eat())
#dog.food()
#print(dog.sound())
#print(cat.eat())
#print(cat.sound())

