# Easy 2
# 1

def greetings(lst, dct):
    full_name = ' '.join(lst)
    title = dct['title']
    occupation = dct['occupation']
    return f"Hello, {full_name}! Nice to have a {title} {occupation} around."

# Second pass:

def greetings(name, job):
    str_name = ' '.join(name)
    return f"Hello, {str_name}! Nice to have a {job["title"]} {job["occupation"]} around."

# 2

name = input("What is your name? ")

if name.endswith('!'):
    print(f"HELLO {name.upper()} WE ARE YELLING!")
else:
    print(f"Hello {name}.")

# Second pass:

name = input("What is your name? ")

if name[-1] == "!": # "Using name[-1] can raise an error if the user just presses Enter (empty string). str.endswith('!') avoids that.""
    print(f"Hello {name.upper()}!!!")
else:
    print(f"Hello {name}.")

# 3

def multiply(num1, num2):
    return num1 * num2

# Second pass same...

# 4

def square(num):
    mult = multiply(num, num)
    mult += multiply(num, num)
    return mult

# Second pass + further exploration:

def multiply(num1, num2):
    return num1 * num2

def square(num):
    return multiply(num, num)

def power(base, exponent):
    result = 1
    for iterations in range(exponent):
        result = multiply(base, result)
    return result

print(power(5, 4))

# 5

float1 = float(input("Enter the first number: "))
float2 = float(input("Enter the second number: "))

print(f"{float1} + {float2} = {float1 + float2}")
print(f"{float1} - {float2} = {float1 - float2}")
print(f"{float1} * {float2} = {float1 * float2}")
print(f"{float1} / {float2} = {float1 / float2}")
print(f"{float1} // {float2} = {float1 // float2}")
print(f"{float1} % {float2} = {float1 % float2}")
print(f"{float1} ** {float2} = {float1 ** float2}")

# Second pass:

def calculate(first, second, func_operator):
        match operator:
            case '+':  return first + second
            case '-':  return first - second
            case '*':  return first * second
            case '/':  return first / second
            case '//': return first // second
            case '%':  return first % second
            case '**': return first ** second
        
num1 = (float(input("==> Enter the first number: ")))
num2 = (float(input("==> Enter the second number: ")))
        
for operator in ['+', '-', '*', '/', '//', '%', '**']:
    result = calculate(num1, num2, operator)
    print(result)

# This could be like this for more info to user:
for operator in ['+', '-', '*', '/', '//', '%', '**']:
    operation = f"{float1} {operator} {float2}"

    result = calculate(float1, float2, operator)

    print(f"==> {operation} = {result}")

# 6

def penultimate(string):
    list_of_str = string.split()
    return list_of_str[-2]

def middle_word(string):
    words = string.split()
    mid = len(words) // 2
    if not words:
        return '.'
    if len(words) == 1:
        return words[0]
    if len(words) % 2 == 0:
        return ' '.join(words[mid - 1:mid + 1])
    if len(words) % 2 != 0:
        return words[mid]
    
# Second pass:

def penultimate(string):
    words = string.split()
    return words[-2]

def middle(string):
    words = string.split()
    mid = len(words) // 2
    
    if len(words) < 3:
        return ' '
    else:
        if len(words) % 2 != 0:
            return words[mid]
        else:
            return words[mid - 1] + ' ' + (words[mid])

print(middle("last blah word") == "blah")
print(middle("Launch School is great!") == "School is")

# 7

def xor(el1, el2):
    if el1 and not el2:
        return True
    if el2 and not el1:
        return True
    return False

# Second pass:
    
def xor(el1, el2):
    if (el1 and not el2) or (el2 and not el1):
        return True

    return False

# 8

def oddities(lst):
    newlst = []
    for i in range(len(lst)):
        if i % 2 == 0:
            newlst.append(lst[i])
    return newlst

# Bonus question:

def oddities(lst):
    return lst[::2]

# Second pass:

def oddities(lst):
    result = []
    for el in range(0, len(lst), 2):
        result.append(lst[el])
    return result

# 9

import random

def name_random_age():
    name = input("What's your name? ").strip()
    if not name:
        print(f"Teddy is {random.randint(20, 100)} years old!")
    else:
        print(f"{name} is {random.randint(20, 100)} years old!")
    
name_random_age()

# Second pass:

from random import randint

name = input("What's your name? ")

if not name:
    print(f"Teddy is {randint(20, 101)} years old!")
else:
    print(f"{name} is {randint(20, 101)} years old!")

# 10

from datetime import datetime as dt

current_year = dt.now().year

age = int(input("What is your age? "))
retirement_age = int(input("At what age would you like to retire? "))
years_until_retirement = retirement_age - age

print(f"It's {current_year}. You will retire in {current_year + years_until_retirement}.")
print(f"You have only {years_until_retirement} years of work to go!")

# Second pass:

from datetime import datetime as dt

age = int(input("What is your age? "))
retire_age = int(input("At what age would you like to retire? "))

print(f"It's {dt.now().year}. You will retire in {dt.now().year + 40}.")
print(f"You have only {retire_age - age} years of work to go!")

# 11

def center_of(string):
    if len(string) % 2 != 0:
        middle_index = len(string) // 2
        return string[middle_index]
    else:
        middle_index = len(string) // 2
        return string[middle_index - 1] + string[middle_index]

# Second pass:

def center_of(string):
    middle = len(string) // 2
    
    if len(string) % 2 != 0:
        return string[middle]
    else:
        return string[middle - 1:middle + 1]
    
# 12

def negative(num):
    if num > 0:
        return (num * -1)
    elif num <= 0:
        return num
    
# Or:
# def negative(num):
#     return -abs(num)

# Second pass:

def negative(num):
    if num < 0:
        return num
    else:
        return -num