# class GoodDog:

#     def __init__(self, name, age):
#         self._name = name
#         self._age = age

#     def speak(self):
#         return f'{self._name} says arf!'
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, name):
#         if not isinstance(name, str):
#             raise TypeError('Name must be a string.')
#         self._name = name

#     @property
#     def age(self):
#         return self._age
    
#     @age.setter
#     def age(self, age):
#         if not isinstance(age, int):
#             raise TypeError('Age must be an integer.')
#         if age < 0:
#             raise ValueError("Age can't be negative.")
#         self._age = age
    
#     # def _dog_years(self):
#     #     return self._age * 7
    
#     # def show_age(self):
#     #     print(f'My age in dog years is {self._dog_years()}')

# print(sparky.name)
# print(sparky.age)

# sparky.name = 'Fireplug'
# print(sparky.name)

# sparky.age = 6
# print(sparky.age)

# These assignments will raise the errors defined in your setters
# sparky.name = 42
# sparky.age = -1

# ###

# class GoodCat():

#     @classmethod
#     def what_am_i(cls):
#         print("I'm a GoodCat class.")

# GoodCat.what_am_i()

###

# class GoodCat:

#     counter = 0 # class variable

#     def __init__(self):
#         GoodCat.counter += 1

#     @classmethod
#     def number_of_cats(cls):
#         return GoodCat.counter
    
#     class ReallyGoodCat(GoodCat):
#         pass

# cat1 = GoodCat()
# cat2 = GoodCat()
# cat3 = ReallyGoodCat()

# print(GoodCat.number_of_cats())        # 3
# print(GoodCat.counter)                 # 3
# print(ReallyGoodCat.number_of_cats())  # 3
# print(ReallyGoodCat.counter)           # 3

###

# class GoodCat:
#     CAT_YEARS = 5

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def human_age(self):
#         return self.age * GoodCat.CAT_YEARS
    
# cocoa = GoodCat('Cocoa', 4)
# print(cocoa.human_age()) # 20

###

# Exercise 1-4, 6:

class Car:
    def __init__(self, model, year, color):
        self._model = model
        self._year = year
        self.color = color
        self.current_speed = 0
        self.engine_is_on = False
        
    def engine_on(self):
        self.engine_is_on = True
        print("Engine on.")

    def accelerate(self):
        if self.engine_is_on:
            self.current_speed += 1
            print(f"Accelerating. Current speed: {self.current_speed} mph.")
        else:
            print("No acceleration; engine is off.")

    def brake(self):
        if self.current_speed > 0:
            self.current_speed -= 1
            print("Braking.")
        else:
            print("The car is stopped.")

    def engine_off(self):
        self.engine_is_on = False
        print("Engine off.")

    def print_current_speed(self):
        print(f"The current speed is {self.current_speed} mph.")

    def model(self):
        return self._model
    
    def year(self):
        return self._year

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, new_color):
        if not isinstance(new_color, str):
            raise TypeError('Color must be a string.')
        self._color = new_color
        print(f'The color is now {new_color}.')

    def spray_paint_car(self, new_color):
        self.color = new_color

    @staticmethod # not from ex1, but still
    def gas_mileage(miles, gallons):
        return miles / gallons

civic = Car('Honda Civic', '2026', 'white')
civic.engine_on()
civic.accelerate()
civic.engine_off()
civic.engine_on()
civic.accelerate()
civic.print_current_speed()

print(civic.model())
print(civic.year())
civic.color = 'Orange'
civic.spray_paint_car('Blue')
print(civic.color)

print(civic.gas_mileage(300, 8))

# Exercise 5:

class Person:
    def __init__(self, first_name, last_name):
        self._set_name(first_name, last_name)

    @property
    def name(self):
        first_name = self._first_name.title()
        last_name = self._last_name.title()
        return f'{first_name} {last_name}'

    @name.setter
    def name(self, name):
        first_name, last_name = name
        self._set_name(first_name, last_name)

    @classmethod
    def _validate(cls, name):
        if not name.isalpha():
            raise ValueError('Name must be alphabetic.')

    def _set_name(self, first_name, last_name):
        Person._validate(first_name)
        Person._validate(last_name)
        self._first_name = first_name
        self._last_name = last_name

actor = Person('Mark', 'Sinclair')
print(actor.name)              # Mark Sinclair
actor.name = ('Vin', 'Diesel')
print(actor.name)              # Vin Diesel
actor.name = ('', 'Diesel')
# ValueError: Name must be alphabetic.