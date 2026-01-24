# 1:
fruits = ("apple", "banana", "cherry", "date", "banana")

print(fruits.count("banana"))

# 3:
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

c = a | b
print(c)

# 5:
ages = {
    "Herman": 32,
    "Lily": 30,
    "Grandpa": 5843,
    "Eddie": 10,
    "Marilyn": 22,
    "Spot": 237,
}

total_age = 0

for age in ages.values():
    total_age += age

print(total_age)

# 6:
print(min(ages.values()))

# 8:
statement = "The Flintstones Rock"

result = {}

for char in statement:
    if char.isalpha():
        result[char] = statement.count(char)

print(result)