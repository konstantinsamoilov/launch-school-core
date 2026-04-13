class Dog:
    def __init__(self, breed):
        self.breed = breed

    @property
    def breed(self):
        return self._breed
    
    @breed.setter
    def breed(self, breed):
        self._breed = breed

golden_retriever = Dog('Golden Retriever')
poodle = Dog('Poodle')
print(golden_retriever.breed)
print(poodle.breed)

samoyed = Dog('Samoyed')
samoyed.breed = 'New Samoyed'

print(samoyed.breed)

class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return "Name not set!"

cat1 = Cat()
print(cat1.get_name())

class Student:
    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name

    @classmethod
    def get_school_name(cls):
        return cls.school_name

student1 = Student('Barbara')
print(student1.__class__.school_name)

student2 = Student('David')
student3 = Student('Victoria')
print(student2.name, student2.__class__.school_name)
print(student3.name, student3.__class__.school_name)

print(Student.get_school_name())
print(Student.school_name)

class Car:
    manufacturer = 'Alfa Romeo'

    def __init__(self, manufacturer_name):
        self.manufacturer = manufacturer_name

    def show_manufacturer(self):
        print(Car.manufacturer)
        print(self.manufacturer)

porsche = Car('Porsche')
porsche.show_manufacturer()

class Bird:
    def __init__(self, species):
        self.species = species

class Sparrow(Bird):
    def __init__(self, species, color):
        super().__init__(species)
        self.color = color

sparrow = Sparrow('sparrow', 'black')
print(sparrow.species)

class Mammal:
    def __init__(self):
        self.legs = 4

class Human(Mammal):
    def __init__(self):
        self.legs = 2

human = Human()
print(human.legs)