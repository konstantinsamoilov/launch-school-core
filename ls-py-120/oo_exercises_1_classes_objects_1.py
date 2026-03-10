# 1

print(type("Hello"))                # <class 'str'>
print(type(5))                      # <class 'int'>
print(type([1, 2, 3]))              # <class 'list'>

# 2-

class Cat:
    def __init__(self):
        print("I'm a cat!")

kitty = Cat()

# 5:

class Cat:
    def __init__(self, name):
        self.name = name
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')

# 6-8:

class Cat:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet()
print(kitty.name)

# 9:

class Cat:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name

    def greet(self):
        print(f"Hello! My name is {self.name}!")

kitty = Cat('Sophie')
kitty.greet()
kitty.name = 'Luna'
kitty.greet()

# 10 (without @property):

class Person:
    def __init__(self, name="John Doe"):
        self.name = name

person1 = Person()
person2 = Person("Pepe Le Pew")

# Comments show expected output
print(person1.name)    # John Doe
print(person2.name)    # Pepe Le Pew