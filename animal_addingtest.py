import unittest
from animal import Animal
from cat import Cat
from dog import Dog

class test_animal(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.cat_1 = Animal('Food','Meow')
        self.dog_1 = Animal('Food','Bark')

    def test_DogEats(self):
        print('test_DogandCat_Eats')
        self.assertEqual(self.cat_1.eats,'Food')

    def test_CatEats(self):
        print('Cat_Eats')
        self.assertEqual(self.dog_1.eats,'Food')

    def test_DogSound(self):
        print('test_DogandCat_Sound')
        self.assertEqual(self.dog_1.sounds,'Bark')
    
    def test_CatSound(self):
        print('test_CatSound')
        self.assertEqual(self.cat_1.sounds,'Meow')

if __name__ == "__main__":
     unittest.main()
    
