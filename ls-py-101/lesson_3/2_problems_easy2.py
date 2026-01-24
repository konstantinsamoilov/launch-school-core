# # Question 1
# numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# reversed_numbers = numbers[::-1]

# reversed_numbers2 = list(reversed(numbers))

# # Question 2

# numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

# number1 = 8  # False (not in numbers)
# number2 = 95 # True (in numbers)

# print(number1 in numbers)
# print(number2 in numbers)

# # Question 3

# print(10 <= 42 <= 100)
# print(10 <= 100 <= 100)
# print(10 <= 101 <= 100)

# print(42 in range(10, 101))
# print(100 in range(10, 101))
# print(101 in range(10, 101))

# Question 4

# numbers = [1, 2, 3, 4, 5]
# del numbers[2] # numbers.pop(2)
# print(numbers)

# Question 5

# numbers = [1, 2, 3, 4]
# table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

# isinstance(numbers, list) # type(numbers) is list
# isinstance(table, list) # type(table) is list

# Question 6

# title = "Flintstone Family Members"

# centered_title = title.center(40)

# Question 7

# statement1 = "The Flintstones Rock!"
# statement2 = "Easy come, easy go."

# print(statement1.count('t'))
# print(statement2.count('t'))

# Question 8

# ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

# print('Spot' in ages)

# Question 9

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 5843, 'Eddie': 10}

additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)
# ages = {**ages, **additional_ages}

print(ages)