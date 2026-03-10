# class Cat:
    
#     def __init__(self, name):
#         self.name = name

#     def __str__(self):
#         return self.name
    
#     def __repr__(self):
#         return f'Cat({repr(self.name)})'
    
#     def __eq__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented
#         return self.name == other.name
    
#     def __ne__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented
#         return self.name != other.name
    
#     def __lt__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented
#         return self.name < other.name
    
#     def __le__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented
#         return self.name <= other.name
    
#     def __gt__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented

#         return self.name > other.name

#     def __ge__(self, other):
#         if not isinstance(other, Cat):
#             return NotImplemented

#         return self.name >= other.name

# cat = Cat('Fuzzy')
# print(str(cat))
# print(repr(cat))

# fuzzy = Cat('Fuzzy')
# fluffy = Cat('Fluffy')
# fluffy2 = Cat('Fluffy')

# print(fuzzy == fluffy)        # False
# print(fluffy == fluffy)       # True
# print(fuzzy != fluffy)        # True
# print(fuzzy != fuzzy)         # False

# print(fluffy == fluffy2)      # True
# print(fluffy != fluffy2)      # False

# whiskers = Cat('Whiskers')

# print(fluffy < whiskers)
# print(fluffy <= whiskers)     # True
# print(fluffy <= fluffy2)      # True
# print(fluffy > whiskers)      # False
# print(fluffy >= whiskers)     # False
# print(fluffy >= fluffy2)      # True

# ###

# class Person:

#     class _Name:

#         def __init__(self, name):
#             self.name = name

#         def __eq__(self, other):
#             return self.name == other.name
        
#         def __ne__(self, other):
#             return self.name != other.name
        
#     def __init__(self, name1, name2):
#         print(self._Name(name1) == self._Name(name2))

# Person('John', 'John')           # True
# Person('Alice', 'Allison')       # False

# ###

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)
    
#     def __iadd__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         self.x += other.x
#         self.y += other.y
#         return self
    
#     def __repr__(self):
#         x = repr(self.x)
#         y = repr(self.y)
#         return f'Vector({x}, {y})'
    
# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2)

# ###

# class MyClass:

#     def __init__(self, x):
#         self.x = x
#         self.y = []
#         self.z = 'xxx'

# obj = MyClass(5)
# print(obj.__dict__)

###
# Exercise 1:

# class Car:

#     def __init__(self, name, year, color):
#         self.name = name
#         self.year = year
#         self.color = color

#     def __str__(self):
#         return f'{self.color.capitalize()} {self.year} {self.name}'

#     def __repr__(self):
#         return f'Car({self.name}, {self.year}, {self.color})'
        
# vwbuzz = Car('ID.Buzz', 2024, 'red')
# print(vwbuzz)        # Red 2024 ID.Buzz
# print(repr(vwbuzz))  # Car('ID.Buzz', 2024, 'red')

# Exercise 2:

# from math import sqrt

# class Vector:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented

#         new_x = self.x + other.x
#         new_y = self.y + other.y
#         return Vector(new_x, new_y)
    
#     def __sub__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         new_x = self.x - other.x
#         new_y = self.y - other.y
#         return Vector(new_x, new_y)
    
#     def __mul__(self, other):
#         if not isinstance(other, Vector):
#             return NotImplemented
        
#         product_1 = self.x * other.x
#         product_2 = self.y * other.y
#         dot_product = product_1 + product_2
#         return dot_product
    
#     def __abs__(self):
#         return sqrt(self.x ** 2 + self.y ** 2)

#     def __repr__(self):
#         x = repr(self.x)
#         y = repr(self.y)
#         return f'Vector({x}, {y})'

# v1 = Vector(5, 12)
# v2 = Vector(13, -4)
# print(v1 + v2) # Vector(18, 8)
# print(v1 - v2) # Vector(-8, 16)
# print(v1 * v2) # 17
# print(abs(v1)) # 13.0

# Exercise 3:
class Candidate:

    def __init__(self, name):
        self.name = name
        self.votes = 0

    def __iadd__(self, other):
        if not isinstance(other, int):
            return NotImplemented

        self.votes += other # this changes the outside-of-Class +=
        return self

class Election:

    def __init__(self, candidates):
        self.candidates = candidates

    def results(self):
        max_votes = 0
        vote_count = 0
        winner = None

        for candidate in candidates:
            vote_count += candidate.votes # Election gets candidate objects created by Class Candidate, so that's where it sees these .votes and .name
            if candidate.votes > max_votes:
                max_votes = candidate.votes
                winner = candidate.name

        for candidate in candidates:
            name = candidate.name
            votes = candidate.votes
            print(f'{name}: {votes} votes')

        percent = 100 * (max_votes / vote_count)
        print()
        print(f'{winner} won: {percent}% of votes')
        
mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes: # votes ends up being these objects with the names of the candidates.
    candidate += 1 # then the iadd method we created can be used anywhere in the program

Election(candidates).results()
# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes