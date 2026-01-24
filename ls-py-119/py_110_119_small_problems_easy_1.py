# Easy 1

# 1

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))
num4 = float(input("Enter the 4th number: "))
num5 = float(input("Enter the 5th number: "))
num6 = float(input("Enter the last number: "))

if num6 in [num1, num2, num3, num4, num5]:
    print(f"{num6} is in {num1, num2, num3, num4, num5}.")
else:
    print(f"{num6} isn't in {num1, num2, num3, num4, num5}.")
# The number collection is in a tuple instead of exactly like the solution is.

# Further exploration:
# LSBot described it as: instead of checking whether the 6th input matches any of the first five numbers, 
# check whether any of the first five numbers meet some condition (here it's greater than 25).

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
num3 = float(input("Enter the 3rd number: "))
num4 = float(input("Enter the 4th number: "))
num5 = float(input("Enter the 5th number: "))

greater_than = any(num > 25 for num in [num1, num2, num3, num4, num5])

if greater_than:
    print("Yes!")
else:
    print("No!")

# 2

def is_palindrome(string):
    if string == string[::-1]:
        return True
    return False

# 3

def is_real_palindrome(string):
    alnum_lower = ''
    
    for char in string:
        if char.isalnum():
            alnum_lower += char
            
    return alnum_lower.casefold() == alnum_lower.casefold()[::-1]

# 4

def running_total(lst):
    result = []
    summed = 0
    
    for num in lst:
        summed += num
        result.append(summed)
        
    return result

# 5

def word_sizes(string):
    lst = string.split()
    counts = {}
    
    for word in lst:
        if len(word) not in counts:
            counts[len(word)] = 1
        else:
            counts[len(word)] += 1
    
    return counts

# 6

def word_sizes(string):
    split_words = string.split()
    alpha_counts = {}

    for word in split_words:
        alpha_word = ''
        for char in word:
            if char.isalpha():
                alpha_word += char         
        if len(alpha_word) not in alpha_counts:
            alpha_counts[len(alpha_word)] = 1
        else:
            alpha_counts[len(alpha_word)] += 1

    return alpha_counts

# 7

def swap(text):
    split_words = text.split()
    swapped_words = []
    
    for word in split_words:
        first_letter = word[0]
        middle = word[1:-1]
        last_letter = word[-1]
        
        if len(word) > 1:
            swapped_word = last_letter + middle + first_letter
            swapped_words.append(swapped_word)
        else:
            swapped_word = first_letter
            swapped_words.append(swapped_word)

    swapped_string = ' '.join(swapped_words)
    return swapped_string

# 8

# This one is interesting. I thought about the integers in ASCII, and if it is possible to build some intra-comparison between the numbers within the program.
# LSBot hinted me that, since the integers are in order, subtracting ord('0') from each number in the parameter will get you the integer of each string number.
# According to LSBot `ord` is not a standard conversion function like `int`, so it's within the rules of the exercise.
# I got to here, a list of the integers we need, but couldn't figure out a way to combine them:

def string_to_integer(string_num):
    ord_num_list = []
    result_list = []

    for el in string_num:
        ord_num_list.append(ord(el))

    for el in ord_num_list:
        result_list.append((el) - ord('0'))
        
    print(result_list)

# LSBot hint version then gave a shorter solution of this kind.
# "For each character, we update value by multiplying the existing value by 10
# (which effectively shifts the existing digits one place to the left) and then adding the new digit."

def string_to_integer(string_num):
    value = 0

    for char in string_num:
        digit = ord(char) - ord('0')
        value = (10 * value) + digit
    return value

print(string_to_integer("4321") == 4321) # value: 4, 43, 432, 4321

# Further exploration:

def hexadecimal_to_integer(hex_string):
    HEX_DIGITS = {
    '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
}
    
    value = 0 
    for char in hex_string.casefold(): # Hexadecimal numbers are case-insensitive
        digit = HEX_DIGITS[char]
        value = (16 * value) + digit
    return value

# 9 (a bit ugly)

def string_to_signed_integer(string_num):
    value = 0

    for el in string_num:
        if el == "+" or el == "-":
            continue
        digit = ord(el) - ord('0')
        value = (10 * value) + digit
        
    if string_num[0] == "+":
        return value
    elif string_num[0] == "-":
        return -value
    else:
        return value
    
# 10
# Creating used_num is kind of ugly, but worked

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def integer_to_string(num):
    result = ''
    
    used_num = num
    
    while used_num > 0:
        quo, rem = divmod(used_num, 10)
        result = DIGITS[rem] + result
        used_num = quo
        
    if num == 0:
        result = DIGITS[0]
        
    return result

# 11

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

def signed_integer_to_string(num):
    result = ''
    used_num = 0
    
    if num > 0:
        used_num = num
    elif num < 0:
        used_num = -num
    else:
        return '0'
    
    while used_num > 0:
        quo, rem = divmod(used_num, 10)
        result = DIGITS[rem] + result
        used_num = quo
        
    if num > 0:
        result = '+' + result
    elif num < 0:
        result = '-' + result  
    return result