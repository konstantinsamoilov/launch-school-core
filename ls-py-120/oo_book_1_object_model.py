class Pet:

    def __init__(self, name):
        self.name = name
        type_name = type(self).__name__ # type_name = self.__class__.__name__
        print(f'I am {name}, a {type_name}.') # I am Sparky, a Dog., etc

    def eat(self):
        print(f"{self.name}: Yum-yum-yum!")

class Dog(Pet):

    def speak(self):
        print(f'{self.name} says Woof!')

    def roll_over(self):
        print(f'{self.name} is rolling over.')

class Cat(Pet):

    def speak(self):
        print(f'{self.name} says Meow!')

class Parrot(Pet):

    def speak(self):
        print(f'{self.name} wants a cracker!')

sparky = Dog('Sparky')
fluffy = Cat('Fluffy')
polly = Parrot('Polly')

sparky.roll_over()

for pet in [sparky, fluffy, polly]:
    pet.speak()
    pet.eat()

# Exercise 1 (Write a program that defines a class and creates two objects from that class. 
# The class should have at least one instance variable that gets initialized by the initializer.)

class DrinksInFrontOfMeRightNow:

    def __init__(self, name):
        self.name = name

class SparklingWater(DrinksInFrontOfMeRightNow):

    def dairy_proportion(self):
        print(f'{self.name} has 0% dairy.')

class Decaf(DrinksInFrontOfMeRightNow):

    def dairy_proportion(self):
        print(f'{self.name} is 15% milk, which Konstantin added.')

class HerbalTea(DrinksInFrontOfMeRightNow):

    def dairy_proportion(self):
        print(f'{self.name} is 20% milk, which Konstantin added.')

grapefruit = SparklingWater('Grapefruit sparkling water')
decaf_cold_brew = Decaf('Decaf cold brew')
vanilla_nut = HerbalTea('Vanilla nut herbal tea')

grapefruit.dairy_proportion()
decaf_cold_brew.dairy_proportion()
vanilla_nut.dairy_proportion()

# Exercise 2 (Given an instance of a Foo object, show two ways to print 'I am a Foo object'
# without hardcoding the word Foo.)

class Foo:

    def __init__(self, name):
        self.name = name
        type_name = self.__class__.__name__
        print(f'I am a {type_name} object')

object1 = Foo('Object 1')
print(f'I am a {type(object1).__name__} object')