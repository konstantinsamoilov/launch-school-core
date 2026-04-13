# Easy 1
# 1:

print(True.__class__)
print((142).__class__)
print(1.23.__class__)
print(True.__class__.__name__)

# 5:

class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

print(vars(Fruit('orange')))
print(vars(Pizza('pepperoni')))
print(vars(Pizza('mushroom')))

cheese = Pizza('cheese')

# 8:

print(cheese.__class__.mro())

for c in cheese.__class__.mro():
    print(c.__name__)

# 10:

class Cat:
    _cats_count = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1

    @classmethod
    def cats_count(cls):
        return cls._cats_count
    
peach = Cat('peach')
charlie = Cat('charlie')
print(Cat.cats_count())

# Easy 2
# 1-2:

class Game:
    _game_count = 0

    def __init__(self):
        self.__class__._game_count += 1

    def play(self):
        return f'Start the {self.game_name} game!'
    
    @property
    def count(self):
        return self.__class__._game_count

class Bingo(Game):
    def __init__(self, game_name, player_name):
        self.game_name = game_name
        self.player_name = player_name
        super().__init__()

class Scrabble(Game):
    def __init__(self, game_name, player_name1, player_name2):
        self.game_name = game_name
        self.player_name1 = player_name1
        self.player_name2 = player_name2
        super().__init__()

bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
# print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'

# 5:

class Greeting:
    def greet(self, message):
        print(message)

class Hello:
    def hi(self):
        self.greet('Hello')

    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet('Hi')

class Goodbye(Greeting):
    def bye(self):
        self.greet('Goodbye')

hello = Hello()
hello.hi()

# 6:

class Cat:
    def __init__(self, type):
        self.type = type

    def __str__(self):
        return f'I am a {self.type}'

print(Cat('hairball'))
# <__main__.Cat object at 0x10695eb10>