class Person:
    name = 'John'

    def get_name(self):
        return self.name
    
alice = Person()
zack = Person()
alice.name = 'Alice'
zack.name = 'Zack'

print(alice.get_name()) # self.name finds the instance variable -> 'Alice'
print(zack.get_name()) # self.name finds the instance variable -> 'Zack'

john = Person()
print(john.get_name()) # self.name finds the CLASS variable -> 'John'
print(Person.name) # class variable -> 'John'

'''
The expression some_instance.some_variable, inside or outside a class, follows the same lookup path: 
instance variables are checked before class variables.

This ambiguity is precisely why the curriculum advises against using self.variable to access class variables. 
It makes the code confusing and potentially buggy if an instance variable of the same name is ever created. 
For clarity, it's always better to use self.__class__.variable or ClassName.variable
when you explicitly intend to work with a class variable.
'''

###

class Person2:
    name = 'leslie'.capitalize() * 3 + '!'
    letters = [letter for letter in 'leslie']

print(Person2.name)
print(Person2.letters)

###

class SwimMixin:
    def enable_swimming(self):
        self.can_swim = True

    def can_i_swim(self):
        if not hasattr(self, 'can_swim'):
            self.can_swim = False

        return self.can_swim

class Dog(SwimMixin):
    # Delete __init__

    def swim(self):
        if self.can_i_swim():
            print('I am swimming!')

teddy = Dog()
teddy.swim()
print('Teddy cannot swim yet.')
teddy.enable_swimming()
print('Teddy can now go swimming.')
teddy.swim() # I am swimming