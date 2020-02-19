from animal import Animal

class Cat(Animal):
   def __init__(self, eats,sounds):
        super().__init__(eats,sounds)

   #def food(self):
        #print(self.name + " eats")  

   def sound(self):
       #print("meow")
       return self.sounds

   def eat(self):
       #print("food")
       return self.eats

cat_1 = Cat("food ", "meow")
# #cat_1.food()
print(cat_1.eat())
print(cat_1.sound())
