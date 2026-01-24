# Easy 3
# 1

def repeat(string, number):
    for num in range(number):
        print(string)

repeat('Hello', 3)

# Second pass:

def repeat(string, repeats):
    for repeats in range(1, repeats + 1): # So yeah when we're dealing with repeat activities, we benefit from ranges starting at 0 and ending one before, can just do that
        print(string)

repeat('Hello', 3)

# 2

def crunch(s):
    result = ''
    for char in s:
        if not result or char != result[-1]:
            result += char
    return result

# Second pass (same, yeah this is by far the easiest):

def crunch(s):
    result = ''
    for char in s:
        if not result or char != result[-1]: # *result* -1, not string
            result += char
    return result

# Further exploration, re.sub & itertools (I didn't know these, LSBot helped):

import re

def crunch(string):
    return re.sub(r'(.)\1+', r'\1', string)

### Or:

from itertools import groupby

def crunch(string):
    return ''.join(key for key, group in groupby(string))
    # groupby groups consecutive identical elements.
    # We take the `key` (the character) from each group.
    # ''.join() combines them back into a string.

# 3

def print_in_box(s):
    horizontal = '+' + ('-' * (len(s) + 2)) + '+'
    message_line = f'| {s} |'
    empty = '| ' + ' ' * len(s) + ' |'
    
    print(horizontal)
    print(empty)
    print(message_line)
    print(empty)
    print(horizontal)

# Second pass:

def print_in_box(string):
    print('+' + '-' * (len(string) + 2) + '+')
    print('|' + ' ' * (len(string) + 2) + '|')
    print('|' + ' ' + string + ' ' + '|')
    print('|' + ' ' * (len(string) + 2) + '|')
    print('+' + '-' * (len(string) + 2) + '+')

# Further exploration 1 first pass:

def print_in_box(s, width = None):
    if width is None:
        inner_content_width = len(s)
    else:
        inner_content_width = max(0, width - 4)
        
    content = s[:inner_content_width]
        
    horizontal = '+' + ('-' * (inner_content_width + 2)) + '+'
    message_line = '| ' + content.ljust(inner_content_width) + ' |'
    empty = '| ' + ' ' * inner_content_width + ' |'
        
    print(horizontal)
    print(empty)
    print(message_line)
    print(empty)
    print(horizontal)

# Further exploration 1 second pass:

def print_in_box(string, width=None):
    if width is None:
        print('+' + '-' * (len(string) + 2) + '+')
        print('|' + ' ' * (len(string) + 2) + '|')
        print('|' + ' ' + string + ' ' + '|')
        print('|' + ' ' * (len(string) + 2) + '|')
        print('+' + '-' * (len(string) + 2) + '+')
    else:
        print('+' + '-' * (width + 2) + '+')
        print('|' + ' ' * (width + 2) + '|')
        print('|' + ' ' + string[:width] + ' ' + '|')
        print('|' + ' ' * (width + 2) + '|')
        print('+' + '-' * (width + 2) + '+')

# Further exploration 2 (I think I didn't do it the first time):
# (Previous code would only be able to handle 2 string lines, I think, so we gotta re-do.)
# LSBot helped fit this into existing code and I simplified it a little):

def print_in_box(string, width=None):
    if width is None:
        content = string
        inner_width = len(content)
        print('+' + '-' * (inner_width + 2) + '+')
        print('|' + ' ' * (inner_width + 2) + '|')
        print('|' + ' ' + content + ' ' + '|')
        print('|' + ' ' * (inner_width + 2) + '|')
        print('+' + '-' * (inner_width + 2) + '+')
        return
    
    # Otherwise:
    lines = wrap_by_words(string, width)
    
    max_line_len = max((len(line) for line in lines), default=0) # getting the padding based on max line length
    
    print('+' + '-' * (max_line_len + 2) + '+')
    print('|' + ' ' * (max_line_len + 2) + '|')
    
    for line in lines:
        padding = ' ' * (max_line_len - len(line))
        print('| ' + line + padding + ' |')
        
    print('|' + ' ' * (max_line_len + 2) + '|')
    print('+' + '-' * (max_line_len + 2) + '+')

def wrap_by_words(string, width):
    if width <= 0:
        return ['']

    words = string.split() # Strings with multiple spaces will not be preserved, sadly
    if not words:
        return ['']

    lines = []
    line = words[0] # Any line will at least be the first word, as a string

    for word in words[1:]:
        if len(line) + 1 + len(word) <= width: # If len(first_word) + 1 (space in-between those two) + len(next_word)...
            line += ' ' + word # first word + ' ' + second word, then check again
        else:
            lines.append(line) # If len(line) + 1 + len(word) > width, add the word / the line to lines
            line = word # Here 'word' gets passed to 'line', and immediately after 'word' becomes another word

    lines.append(line) # This line is here because the loop is unable to append the last line within the loop, we need to come out to do it
    return lines

# string: "Konstantin is doing a further exploration exercise"
# width: 20

# Start line = "Konstantin" (len 11)
# Try "is": 11 + 1 + 2 = 14 → fits → "Konstantin is"
# Try "doing": 14 + 1 + 5 = 20 → fits → "Konstantin is doing"
# Try "a": 20 + 1 + 1 = 22 → doesn’t fit → append current line, start new line with "a"
# Try "further": "a" (1) + 1 + 7 = 9 → fits → "a further"
# Try "exploration": 9 + 1 + 11 = 21 → doesn’t fit → append "a further", start "exploration"
# Try "exercise": "exploration" (11) + 1 + 9 = 21 → doesn’t fit → append "exploration", start "exercise"
# Append the final line "exercise"
# So wrap_by_words returns: ["Konstantin is doing", "a further", "exploration", "exercise"]

# 4

def stringy(num):
    if num % 2 == 0:
        return "10" * (num // 2)
    else:
        return "10" * (num // 2) + '1' # this is so insane

# Second pass:

def stringy(num):
    result = ''
    i = 0

    while i < num:
        if i % 2 != 0:
            result += '0'
        else:
            result += '1'
        i += 1
        
    return result

# 5

def triangle(num):
    for el in range(1, num + 1):
        print(' ' * (num - el) + '*' * el)
    
# Second pass:
# Yeah, because you need an "i" iterator inside the loop, it's good to name your parameter something real like "height" for some clarity 
def triangle(height):
    for i in range(1, height + 1):
        spaces = height - i
        stars = i
        print((' ' * spaces) + ('*' * stars))

# 6

noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")

print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
print(f"The {adjective} {noun} {verb} {adverb} over the lazy {noun}.")
print(f"The {noun} {adverb} {verb} up to Joe's {adjective} turtle.")

# Skipping second pass of 6

# 7 (I probably couldn't figure it out and retyped it)

def is_double_num(num):
    num_string = str(num)
    center = len(num_string) // 2
    left_number = num_string[:center]
    right_number = num_string[center:]
        
    return left_number == right_number
        
def twice(num):   
    if is_double_num(num):
        return num
    else:
        return num * 2

# Second pass: (still needed help but less so)

def twice(num):
    mid = len(str(num)) // 2
    mid_idx = int(mid) # these two lines are kind of funny
    
    if len(str(num)) % 2 != 0:
        return num * 2
    elif str(num)[:mid_idx] != str(num)[mid_idx:]:
        return num * 2
    else:
        return num
    
# 8

def get_grade(g1, g2, g3):
    score = (g1 + g2 + g3) / 3
    
    if 90 <= score <= 100:
        return 'A'
    elif 80 <= score < 90: 
        return 'B'
    elif 70 <= score < 80: 
        return 'C'
    elif 60 <= score < 70: 
        return 'D'
    else:
        return 'F'
    
# Skipping second pass of 8

# 9

def clean_up(string):
    result = ''
    
    for char in string:
        if char.isalpha():
            result += char
        else:
            if len(result) == 0:
                result += ' '
            elif result[-1] != ' ':
                result += ' '
                
    return result

# Second pass (aside from doing these in study sessions...)
# Still couldn't do it but got closer. Wanted this to work:

def clean_up(string):
    alphas_spaces = ''
    
    for char in string:
        if char.isalpha() or char.isspace():
            alphas_spaces += char
        else:
            alphas_spaces += ' '
    
    print(alphas_spaces) # '   what s my     line ', but then you're left with the same kinda problem
    
    result_list = alphas_spaces.split()
    result = ' '.join(result_list) # when regina george said stop trying to make fetch happen it was about this solution
    
    return result

# The best solution I've seen is:

def clean_up(text):
    result = ''
    for char in text:
        if char.isalpha():
            result += char
        elif not result or result[-1] != ' ':
            result += ' '
    return result

# 10 (I think not much of this was 'mine')

def century(year):
    century_number = (year - 1) // 100 + 1
    last_two = century_number % 100
    
    if last_two in (11, 12, 13):
        suffix = 'th'
    else:
        last_digit = century_number % 10
        if last_digit == 1:
            suffix = 'st'
        elif last_digit == 2:
            suffix = 'nd'
        elif last_digit == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
            
    return f"{century_number}{suffix}"

# Second pass (the century math in one line I still couldn't figure out):

def century(year):
    century_result_num = (year - 1) // 100 + 1
    century_result = str(century_result_num)
    
    if century_result.endswith(('11', '12', '13')):
        return century_result + 'th'
    elif century_result.endswith('1'):
        return century_result + 'st'
    elif century_result.endswith('2'): 
        return century_result + 'nd'
    elif century_result.endswith('3'): 
        return century_result + 'rd'
    else:
        return century_result + 'th'