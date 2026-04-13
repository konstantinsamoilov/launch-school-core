# 2 and 3:

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() == other.name.lower()
    
    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() != other.name.lower()
    
    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() > other.name.lower()
    
    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() < other.name.lower()
    
    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() >= other.name.lower()
    
    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.lower() <= other.name.lower()
    
peach = Cat('Peach')
carrie = Cat('Carrie')

print(peach == carrie)
print(peach != carrie)
print(peach == 'peach') # NotImplemented both ways, so falls back to 'peach is 'peach'', which is False
print('')
print(peach > carrie)
print(peach <= carrie)
# print(carrie > 'carrot') # TypeError: '>' not supported between instances of 'Cat' and 'str'

# 4:

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Vector({self.x}, {self.y})'
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    # these usually should be in pairs with their r-versions but i left them out here
    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)
    
    def __rmul__(self, other):
        return Vector(self.x * other, self.y * other)

print(Vector(3, 2) + Vector(5, 12))   # Vector(8, 14)
print(Vector(5, 12) - Vector(3, 2))   # Vector(2, 10)
print(Vector(5, 12) * 2)              # Vector(10, 24)
print(3 * Vector(5, 12))              # Vector(15, 36)

my_vector = Vector(5, 7)
my_vector += Vector(3, 9)
print(my_vector)                      # Vector(8, 16)

my_vector -= Vector(1, 7)
print(my_vector)                      # Vector(7, 9)

# print(Vector(3, 2) + 5)
# TypeError: unsupported operand type(s) for +: 'Vector' and 'int'

# 5:

class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __add__(self, other):
        if not isinstance(other, (int, str)):
            return NotImplemented
        
        if (isinstance(self.value, int) or isinstance(self.value, str) and self.value.isdigit()) \
        and (isinstance(other, int) or isinstance(other, str) and other.isdigit()):
            return Silly(int(self.value) + int(other))
        else:
            return Silly(str(self.value) + str(other))

    def __str__(self):
        return f'Silly({repr(self.value)})'

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)