# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __eq__(self, other):            # self == other
#         if not isinstance(other, Person):
#             return NotImplemented

#         return self.age == other.age

#     def __ne__(self, other):            # self != other
#         if not isinstance(other, Person):
#             return NotImplemented

#         return self.age != other.age

#     def __lt__(self, other):            # self < other
#         if not isinstance(other, Person):
#             return NotImplemented

#         return self.age < other.age
    
#     def __gt__(self, other):            # self > other
#         if not isinstance(other, Person):
#             return NotImplemented

#         return self.age > other.age
    
#     def __le__(self, other):            # self <= other
#         if not isinstance(other, Person):
#             return NotImplemented

#         return self.age <= other.age

#     def __ge__(self, other):            # self >= other
#         if not isinstance(other, Person):
#             return NotImplemented

#         return self.age >= other.age

# ted = Person('Ted', 33)
# carol = Person('Carol', 49)

# if ted < carol:
#     print('Ted is younger than Carol')
# else:
#     print('Ted is older than Carol')

###

class Person:
    def __init__(self, name):
        self.name = name

class Team:
    def __init__(self, name, persons=[]):
        self.name = name
        self.members = persons

    def __add__(self, other_team):
        if not isinstance(other_team, Team):
            return NotImplemented

        team_members = self.members + other_team.members
        return Team('Temporary Team', team_members)
    
    def __iadd__(self, other_team):
        if not isinstance(other_team, Team):
            return NotImplemented
        
        self.members += other_team.members
        return self

cowboys = Team(
    'Dallas Cowboys',
    [
        Person('Troy Aikman'),
        Person('Emmitt Smith'),
        Person('Michael Irvin'),
    ]
)

niners = Team(
    'San Francisco 49ers',
    [
        Person('Joe Montana'),
        Person('Jerry Rice'),
        Person('Deion Sanders'),
    ]
)
# +
dream_team = niners + cowboys

print(dream_team.name)
for person in dream_team.members:
    print(person.name)

# +=
dream_team = Team('Dream Team')
dream_team += cowboys
dream_team += niners

for person in dream_team.members:
    print(person.name)