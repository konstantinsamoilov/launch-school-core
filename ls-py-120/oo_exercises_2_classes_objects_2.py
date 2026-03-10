# 1:

class Cat:
    @classmethod
    def generic_greeting(cls):
        print("Hello! I'm a cat!")
        
kitty = Cat()
type(kitty).generic_greeting()

# 2:

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
    def rename(self, new_name):
        self.name = new_name

kitty = Cat('Sophie')
print(kitty.name)             # Sophie
kitty.rename('Chloe')
print(kitty.name)             # Chloe

# 3:

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        
    def identify(self):
        return self

kitty = Cat('Sophie')
print(kitty.identify())
# <__main__.Cat object at 0x10508c8d0> # The object ID (0x105...) may vary

# 4:

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def personal_greeting(self):
        print(f'Hello! My name is {self._name}!')

kitty = Cat('Sophie')
kitty.personal_greeting()     # Hello! My name is Sophie!

# 5:

class Cat:
    cats = 0
    
    def __init__(self):
        Cat.cats += 1
    
    @classmethod
    def total(cls):
        print(cls.cats)

Cat.total()         # 0

kitty1 = Cat()
Cat.total()         # 1

kitty2 = Cat()
Cat.total()         # 2

print(Cat())        # <__main__.Cat object at 0x104ed7290>
Cat.total()         # 3

# 6:

class Cat:
    COLOR = 'purple'
    
    def __init__(self, name):
        self._name = name
        
    def greet(self):
        print(f"Hello! My name is {self._name} and I'm a {Cat.COLOR} cat!")
        
sophie = Cat('Sophie')
sophie.greet()

# 7:

class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    def __repr__(self):
        return f"I'm {self._name}!"

# Comments show expected output
kitty = Cat('Sophie')
print(kitty)        # I'm Sophie!