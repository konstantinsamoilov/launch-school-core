class Vehicle:

    def __init__(self, wheels):
        self._wheels = wheels
        print(f'I have {self._wheels} wheels.')

    def drive(self):
        print('I am driving.')

class Car(Vehicle):
    
    def __init__(self):
        print('Creating a car.')
        super().__init__(4)

class Truck(Vehicle):

    def __init__(self):
        print('Creating a truck.')
        super().__init__(18)

class Motorcycle(Vehicle):

    def __init__(self):
        print('Creating a motorcycle.')
        super().__init__(2)

    def drive(self):
        super().drive()
        print('No! I am riding!')

car = Car()
car.drive()
print()

truck = Truck()
truck.drive()
print()

motorcycle = Motorcycle()
motorcycle.drive()

###

class Pet:

    def play(self):
        print('I am playing')

class Predator:

    def hunt(self):
        print('I am hunting')

class Cat(Pet, Predator):

    def purr(self):
        print('I am purring')

cat = Cat()
cat.purr()          # I am purring
cat.play()          # I am playing
cat.hunt()          # I am hunting

###

'''
class ColorMixin:

    def set_color(self, color):
        self._color = color

    def get_color(self):
        return self._color
'''

from color_mixin import ColorMixin

class Car(ColorMixin):

    def __init__(self, color):
        self.set_color(color)
    
car = Car('red')
print(car.get_color())

car.set_color('green')
print(car.get_color())

class SmartLight:

    def __init__(self, color):
        self.set_color(color)

smart_light = SmartLight('cool white')
print(smart_light.get_color())   # cool white

smart_light.set_color('goldenrod')
print(smart_light.get_color())   # goldenrod

class House:

    def __init__(self, color):
        self.set_color(color)

house = House('sky blue')
print(house.get_color())         # sky blue

house.set_color('lavender')
print(house.get_color())         # lavender

###

class Shape:

    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self, width, height):
        self._width = width
        self._height = height

    def set_width(self, width):
        self._width = width

    def set_height(self, height):
        self._height = height

    def area(self):
        my_area = self._width * self._height
        print(f'area is {my_area}')

class Square(Shape):

    def __init__(self, size):
        self._size = size

    def set_size(self, size):
        self._size = size

    def area(self):
        my_area = self._size * self._size
        print(f'area is {my_area}')

square = Square(7)
square.area()

square.set_size(12)
square.area()

square.width = 5
square.height = 9
square.area()

###

class Shape:

    def __init__(self, width, height):
        self.set_size(width, height)

    def set_size(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        my_area = self.width * self.height
        print(f'area is {my_area}')

class Rectangle:

    def __init__(self, width, height):
        self._shape = Shape(width, height)

    def set_width(self, width):
        self._shape.set_size(width, self._shape.height)

    def set_height(self, height):
        self._shape.set_size(self._shape.width, height)

    def area(self):
        self._shape.area()

class Square:

    def __init__(self, size):
        self._shape = Shape(size, size)

    def set_size(self, size):
        self._shape.set_size(size, size)

    def area(self):
        self._shape.area()

###

class LandDwellingMixin:
    pass

class LanguageMixin:
    pass

class BipedalismMixin:
    pass

class Creature:
    pass

class Mammal(Creature):
    pass

class Primate(LandDwellingMixin, Mammal):
    pass

class Human(BipedalismMixin,
            LanguageMixin,
            Primate):
    pass

print(Human.mro())

# Pretty printed for clarity
# [
#     <class '__main__.Human'>,
#     <class '__main__.BipedalismMixin'>,
#     <class '__main__.LanguageMixin'>,
#     <class '__main__.Primate'>,
#     <class '__main__.LandDwellingMixin'>,
#     <class '__main__.Mammal'>,
#     <class '__main__.Creature'>,
#     <class 'object'>
# ]

# Exercise 2, 3, 4:

class Vehicle:

    vehicle_counter = 0

    def __init__(self):
        Vehicle.vehicle_counter += 1

    @classmethod
    def vehicles(cls):
        return Vehicle.vehicle_counter
    
class SignalMixin:

    def signal_left(self):
        left_signal = True
        right_signal = False
        print("Signalling left")

    def signal_right(self):
        left_signal = False
        right_signal = True
        print("Signalling right")

    def signal_off(self):
        left_signal = False
        right_signal = False
        print("Signal is now off")

class Car(SignalMixin, Vehicle):

    def __init__(self):
        super().__init__()

class Truck(SignalMixin, Vehicle):

    def __init__(self):
        super().__init__()

class Boat(Vehicle):

    def __init__(self):
        super().__init__()

print(Car.vehicles())     # 0
car1 = Car()
print(Car.vehicles())     # 1
car2 = Car()
car3 = Car()
car4 = Car()
print(Car.vehicles())     # 4
truck1 = Truck()
truck2 = Truck()
print(Truck.vehicles())   # 6
boat1 = Boat()
boat2 = Boat()
print(Boat.vehicles())    # 8

car1.signal_left()       # Signalling left
truck1.signal_right()    # Signalling right
car1.signal_off()        # Signal is now off
truck1.signal_off()      # Signal is now off
# boat1.signal_left()
# AttributeError: 'Boat' object has no attribute 'signal_left'

print(Car.mro())
print(Truck.mro())
print(Boat.mro())
print(Vehicle.mro())

# Exercise 5:

class Vehicle:

    def __init__(self, fuel_capacity, mpg):
        self.capacity = fuel_capacity
        self.mpg = mpg

    def max_range_in_miles(self):
        return self.capacity * self.mpg

class Car(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)

    def family_drive(self):
        print('Taking the family for a drive')

class Truck(Vehicle):

    def __init__(self, fuel_capacity, mpg):
        super().__init__(fuel_capacity, mpg)        

    def hookup_trailer(self):
        print('Hooking up trailer')

car = Car(12.5, 25.4)
truck = Truck(150.0, 6.25)

print(car.max_range_in_miles())         # 317.5
print(truck.max_range_in_miles())       # 937.5

car.family_drive()     # Taking the family for a drive
truck.hookup_trailer() # Hooking up trailer

try:
    truck.family_drive()
except AttributeError:
    print('No family_drive method for Truck')
# No family_drive method for Truck

try:
    car.hookup_trailer()
except AttributeError:
    print('No hookup_trailer method for Car')
# No hookup_trailer method for Car