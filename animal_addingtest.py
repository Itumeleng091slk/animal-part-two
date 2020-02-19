import unittest
from animal import Animal
from cat import Cat
from dog import Dog

class test_animal(unittest.TestCase):
    def setUp(self):
        print('Pass')
        self.cat_1 = Animal('Food','Meow')
        self.dog_1 = Animal('Food','Bark')

    def test_DogEats(self):
        print('Does dog eat food')
        self.assertEqual(self.cat_1.eats,'Food')

    def test_CatEats(self):
        print('Does cat eat food')
        self.assertEqual(self.dog_1.eats,'Food')

    def test_DogSound(self):
        print('Does the dog bark')
        self.assertEqual(self.dog_1.sounds,'Bark')
    
    def test_CatSound(self):
        print('Does the cat meow')
        self.assertEqual(self.cat_1.sounds,'Meow')

if __name__ == "__main__":
     unittest.main()
    
