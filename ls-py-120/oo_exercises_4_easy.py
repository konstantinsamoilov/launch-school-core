# 1 + further exploration:

class Banner:
    def __init__(self, message, banner_width=False):
        self.message = message
        self.banner_width = banner_width

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        if not self.banner_width:
            return f"|{' ' * (len(self.message) + 2)}|"
        else:
            return f"|{' ' * (self.banner_width - 2)}|"

    def _horizontal_rule(self):
        if not self.banner_width:
            return f"+{'-' * (len(self.message) + 2)}+"
        else:
            return f"+{'-' * (self.banner_width - 2)}+"

    def _message_line(self):
        if not self.banner_width:
            return f"| {self.message} |"
        elif self.banner_width < 5:
            return f"|{' ' * (self.banner_width - 2)}|"
        elif self.banner_width % 2 == 1:
            return f"|{' ' * ((self.banner_width - 3) // 2)}{self.message[:self.banner_width - 4]}{' ' * ((self.banner_width - 4) // 2)}|"
        elif self.banner_width % 2 == 0:
            return f"|{' ' * ((self.banner_width - 3) // 2)}{self.message[:self.banner_width - 4]}{' ' * ((self.banner_width - 3) // 2)}|"

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+

banner = Banner('To boldly go where no one has gone before.', 2)
print(banner)

banner = Banner('Hi', 25)
print(banner)

banner = Banner('Hi', 6)
print(banner)

# 2:

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    @property
    def area(self):
        return self.width * self.height

rect = Rectangle(4, 5)

print(rect.width == 4)        # True
print(rect.height == 5)       # True
print(rect.area == 20)        # True

# 3:

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @property
    def area(self):
        return self._width * self._height
    
class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# 4:

class Pet:
    def __init__(self, name, age, color):
        self._name = name
        self._age = age
        self._color = color

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age
    
    @property
    def color(self):
        return self._color

class Cat(Pet):
    @property
    def info(self):
        return (f"My cat {self.name} is {self.age} "
                f"years old and has {self.color} fur.")

cocoa = Cat('Cocoa', 3, 'black')
cheddar = Cat('Cheddar', 4, 'yellow and white')

print(cocoa.info)
print(cheddar.info)

# 5:

class Animal:
    def __init__(self, name, age, legs, species, status):
        self.name = name
        self.age = age
        self.legs = legs
        self.species = species
        self.status = status

    def introduce(self):
        return (f"Hello, my name is {self.name} and I am "
                f"{self.age} years old and {self.status}.")
        
class Cat(Animal):
    def __init__(self, name, age, status):
        super().__init__(name, age, 4, 'cat', status)

    def introduce(self):
        return super().introduce() + " Meow meow!"
    
class Dog(Animal):
    def __init__(self, name, age, status, owner):
        super().__init__(name, age, 4, 'dog', status)
        self.owner = owner
        
    def introduce(self):
        return super().introduce() + " Woof! Woof!"
    
    def greet_owner(self):
        return f"Hi {self.owner}! Woof! Woof!"
        
cat = Cat("Pepe", 4, "happy")
expected = ("Hello, my name is Pepe and I am 4 years old "
            "and happy. Meow meow!")
print(cat.introduce() == expected)      # True

dog = Dog("Bobo", 9, "hungry", "parent")
expected = ("Hello, my name is Bobo and I am 9 years old "
            "and hungry. Woof! Woof!")
print(dog.introduce() == expected)                  # True
print(dog.greet_owner() == "Hi parent! Woof! Woof!") # True

# 6:

class Pet:
    def __init__(self, animal, name):
        self.animal = animal
        self.name = name

class Owner:
    def __init__(self, name):
        self.name = name
        self.pets = []
        
    def number_of_pets(self):
        return len(self.pets)
        
    def print_pets(self):
        for pet_of_owner in self.pets:
            print(f"a {pet_of_owner.animal} named {pet_of_owner.name}")
        
class Shelter:
    def __init__(self):
        self.owners = set()
    
    def adopt(self, owner, pet):
        owner.pets.append(pet)
        self.owners.add(owner)
        
    def print_adoptions(self):
        for owner in self.owners:
            print(f"{owner.name} has adopted the following pets:")
            owner.print_pets()
            print("")

cocoa   = Pet('cat', 'Cocoa')
cheddar = Pet('cat', 'Cheddar')
darwin  = Pet('bearded dragon', 'Darwin')
kennedy = Pet('dog', 'Kennedy')
sweetie = Pet('parakeet', 'Sweetie Pie')
molly   = Pet('dog', 'Molly')
chester = Pet('fish', 'Chester')

phanson = Owner('P Hanson')
bholmes = Owner('B Holmes')

shelter = Shelter()
shelter.adopt(phanson, cocoa)
shelter.adopt(phanson, cheddar)
shelter.adopt(phanson, darwin)
shelter.adopt(bholmes, kennedy)
shelter.adopt(bholmes, sweetie)
shelter.adopt(bholmes, molly)
shelter.adopt(bholmes, chester)

shelter.print_adoptions()
print(f"{phanson.name} has {phanson.number_of_pets()} "
      "adopted pets.")
print(f"{bholmes.name} has {bholmes.number_of_pets()} "
      "adopted pets.")

# 7:

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        
    def info(self):
        return f"{self.make} {self.model}"
    
    def get_wheels(self):
        raise NotImplementedError("Subclasses must implement get_wheels.")

class Car(Vehicle):
    def get_wheels(self):
        return 4

class Motorcycle(Vehicle):
    def get_wheels(self):
        return 2

class Truck(Vehicle):
    def __init__(self, make, model, payload):
        super().__init__(make, model)
        self.payload = payload

    def get_wheels(self):
        return 6
    
# 8:

class Creature:
    def walk(self):
        return f"{self.name} {self.gait()} forward"

class Person(Creature):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(Creature):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(Creature):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"
    
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"

# 9:

class WalkMixin:
    def walk(self):
        return f"{self} {self.gait()} forward"
    
class Animal:
    def __str__(self):
        return self.name

class Person(WalkMixin, Animal):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "strolls"

class Cat(WalkMixin, Animal):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "saunters"

class Cheetah(WalkMixin, Animal):
    def __init__(self, name):
        self.name = name

    def gait(self):
        return "runs"

class Noble(WalkMixin, Animal):
    def __init__(self, name, title):
        self.name = name
        self.title = title
        
    def __str__(self):
        return f"{self.title} {self.name}"
    
    def gait(self):
        return "struts"
    
mike = Person("Mike")
print(mike.walk())  # Expected: "Mike strolls forward"

kitty = Cat("Kitty")
print(kitty.walk())  # Expected: "Kitty saunters forward"

flash = Cheetah("Flash")
print(flash.walk())  # Expected: "Flash runs forward"
    
byron = Noble("Byron", "Lord")
print(byron.walk())  # "Lord Byron struts forward"
print(byron.name)    # "Byron"
print(byron.title)   # "Lord"

# 10:

class House:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value
        
    def __lt__(self, other_home):
        if isinstance(other_home, House):
            return self.price < other_home.price
        
        return NotImplemented
    
    def __gt__(self, other_home):
        if isinstance(other_home, House):
            return self.price > other_home.price
        
        return NotImplemented

home1 = House(100000)
home2 = House(150000)
if home1 < home2:
    print("Home 1 is cheaper")
if home2 > home1:
    print("Home 2 is more expensive")

# 11:

class Wallet:
    def __init__(self, amount):
        self.amount = amount
        
    def __add__(self, second_wallet):
        added_amount = self.amount + second_wallet.amount
        return Wallet(added_amount)

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet.amount == 80)       # True

# 12:

class Wallet:
    def __init__(self, amount):
        self.amount = amount

    def __add__(self, other):
        return Wallet(self.amount + other.amount)
    
    def __str__(self):
        return f"Wallet with ${self.amount}"

wallet1 = Wallet(50)
wallet2 = Wallet(30)
merged_wallet = wallet1 + wallet2
print(merged_wallet)          # Wallet with $80.

# 13:

class Transform:
    def __init__(self, text):
        self.text = text
        
    def uppercase(self):
        return self.text.upper()
    
    @staticmethod
    def lowercase(text):
        return text.lower()

my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz