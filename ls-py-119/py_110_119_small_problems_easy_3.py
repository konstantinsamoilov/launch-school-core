# 1:

"""
Problem:
input: integer (minutes)
output: string of a 24hr time

explicit rules: 
1. returns in hh:mm format.
2. can't use datetime.
3. disregard daylight savings and standard time.

implicit rules: 
1. if input is positive, the output "goes forward", and vice versa.

questions: 
what if input integer is more (either way) than the 1440 minutes in a day?

Examples:
if integer is >= 1440 / <= -1440, it keeps looping around.

Data structures:
Integers, strings, maybe a for loop, maybe holder variable for the minutes because they keep looping

A:
Create constants for minutes in a day and minutes in an hour.
-> Turns out we don't need them.

Accept integer input as minutes.

For positive integers:
Do floor division // on minutes by 60 to get the hours.
Divide with remainder % on minutes by 60 to get the minutes.

If hours are == 24:
    Return '00'

While hours are >= 24:
    Subtract 24 from hours.

While hours are < 0:
    Add 24 to hours.

If hours < 10 or rem_minutes < 10, reassign them to '0' + str(int).
If not, just reassign them to str(int).

Return f-string of hours and rem_minutes with : in the middle.
"""

def time_of_day(minutes):
    hours = minutes // 60
    rem_minutes = minutes % 60

    while hours >= 24:
        hours -= 24

    while hours < 0:
        hours += 24

    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)

    if rem_minutes < 10:
        rem_minutes = '0' + str(rem_minutes)
    else:
        rem_minutes = str(rem_minutes)

    return f'{hours}:{rem_minutes}'

print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# Further exploration:

# How would you approach this problem if you could use Python's datetime class? Suppose you also needed to consider the day of the week?
# (Assume that delta_minutes is the number of minutes before or after midnight between Saturday and Sunday;
# in such a function, a delta_minutes value of -4231 would need to produce a return value of Thursday 01:29.)

# Without datetime:

MINUTES_PER_DAY = 1440
DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

def time_of_day(minutes):
    hours = minutes // 60
    rem_minutes = minutes % 60
    
    days_offset = minutes // MINUTES_PER_DAY
    day_index = days_offset % 7
    day_name = DAYS[day_index]

# -2 % 7, for instance:
# The cycle is 0 to 6, because the remainder has to be less than 7.
# We start at 0, and go backward 2 steps:
# 0 -> 6 -> 5. The result is 5.
    
    while hours >= 24:
        hours -= 24

    while hours < 0:
        hours += 24

    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)

    if rem_minutes < 10:
        rem_minutes = '0' + str(rem_minutes)
    else:
        rem_minutes = str(rem_minutes)

    print(f'{day_name} {hours}:{rem_minutes}')

time_of_day(0) # Sunday 00:00
time_of_day(-3) # Saturday 23:57
time_of_day(35) # Sunday 00:35
time_of_day(-1437) # Saturday 00:03
time_of_day(3000) # Tuesday 02:00
time_of_day(800) # Sunday 13:20
time_of_day(-4231) # Thursday 01:29

# With datetime:

from datetime import datetime, timedelta

def time_of_day(minutes):
    hours = minutes // 60
    rem_minutes = minutes % 60
    
    start_of_week = datetime(2026, 1, 11)
    time_delta = timedelta(minutes=minutes)
    final_datetime = start_of_week + time_delta

    while hours >= 24:
        hours -= 24

    while hours < 0:
        hours += 24

    if hours < 10:
        hours = '0' + str(hours)
    else:
        hours = str(hours)

    if rem_minutes < 10:
        rem_minutes = '0' + str(rem_minutes)
    else:
        rem_minutes = str(rem_minutes)

    print(final_datetime.strftime("%A %H:%M"))

time_of_day(0) # Sunday 00:00
time_of_day(-3) # Saturday 23:57
time_of_day(35) # Sunday 00:35
time_of_day(-1437) # Saturday 00:03
time_of_day(3000) # Tuesday 02:00
time_of_day(800) # Sunday 13:20
time_of_day(-4231) # Thursday 01:29

# 2: 

'''
input: string (time)
output: integer

rules: 1. input is time in 24-hour format
2. return is minutes before / after midnight
3. should return an integer from 0-1439
4. can't use datetime module
5. disregard daylight savings and standard time

data: strings, integers

algorithm (after midnight):
make a 'MINUTES_IN_DAY' constant, set to 1440
make a 'result' integer, set to 0

if time input is 24:00, return 0
otherwise:

split input string on the :, save to a list

turn strings in list into integers with constructors, using a for loop
reassign new list to variable

for integer at index 0, multiply it by 60 and add it to result
for integer at index 1, add it to result

if result is over 1440, subtract 1440 from result until it's not
return result

algorithm (before midnight):
Do the backwards version of after_midnight.
still make a 'MINUTES_IN_DAY' constant, set to 1440
make a 'result' integer, set to 1440
subtract from result instead of adding.
'''

def after_midnight(time_of_day):
    MINUTES_IN_DAY = 1440
    result = 0
    
    time_list = time_of_day.split(':')
    
    time_list_ints = []
    for el in time_list:
        time_list_ints.append(int(el))
    
    result += (time_list_ints[0] * 60) + time_list_ints[1]
    
    if result == MINUTES_IN_DAY:
        return 0
    else:
        return result
    
def before_midnight(time_of_day):
    MINUTES_IN_DAY = 1440
    result = 1440
    
    time_list = time_of_day.split(':')
    
    time_list_ints = []
    for el in time_list:
        time_list_ints.append(int(el))
    
    result -= (time_list_ints[0] * 60) + time_list_ints[1]
    
    if result == MINUTES_IN_DAY:
        return 0
    else:
        return result
    
''' Or this:
def before_midnight(time_of_day):
    minutes_after = after_midnight(time_of_day)
    minutes_before = MINUTES_IN_DAY - minutes_after
    return 0 if minutes_before == MINUTES_IN_DAY else minutes_before
'''

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True

# Further exploration (with datetime.datetime)

from datetime import datetime

MINUTES_IN_DAY = 1440

def after_midnight(time_of_day):
    if time_of_day == "24:00":
        return 0
    
    time_obj = datetime.strptime(time_of_day, "%H:%M")
    print(time_obj) # 1900-01-01 21:23:00
    print(time_obj.hour * 60 + time_obj.minute)
    return time_obj.hour * 60 + time_obj.minute

print(after_midnight("21:23") == 1283)

# 3:

'''
input: string
output: string

rules: doubles every character in string
returns result as new string

implicit rules: if input is empty, output is empty

question: does it somehow someway double the quotation marks too? or do they just happen to be doubled in the test case results?

data: strings, maybe lists

algorithm:
create a result variable, set to empty string

use a for loop to iterate over each character, and add that character, times 2, to result

return result
'''

def repeater(s):
    result = ''
    
    for char in s:
        result += char * 2

    print(repr(result)) # 'HHeelllloo'
    return result
        
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True

# 4:

'''
input: string
output: string

rules: double every consonant in string and return that new string
don't double vowels, digits, punctuation, whitespace
only ASCII characters will be passed into function

data: strings

algorithm: make empty string 'result'
make a 'vowels' string constant, lowercase and uppercase

use a for loop to iterate over characters in the string
filter for alphabetical characters and those not in the vowels string
add passing characters times 2 to result string
add failing characters times 1 to result string

return result string
'''

def double_consonants(s):
    result = ''
    VOWELS = 'aeiouAEIOU'
    
    for char in s:
        if char.isalpha() and char not in VOWELS:
            result += char * 2
        else:
            result += char
            
    return result

# All of these examples should print True
print(double_consonants('String') == "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")

# 5:

'''
input: positive integer
output: positive integer

rules: takes positive integer, returns digit-reversed integer
implicit rules: if input integer ends in a 0, the reverse version will not start with a 0, it will instead be shorter

data: integers, maybe strings, maybe lists

algorithm: convert input integer to string, with a constructor, and point it to a variable
reverse the string using slicing, point it to the variable
convert the string to an integer with a constructor
return the integer
'''

def reverse_number(num):
    str_num = str(num)
    str_num = str_num[::-1]
    result = int(str_num)
    return result

print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True

# 6:

'''
input: integer
output: list

rules: takes integer arg, returns list with all integers 1 to integer arg, inclusive, in ascending order
arg will always be positive integer

data: integer, list

algorithm:
create a range object from 1 to integer argument + 1, and point it to a 'result' variable
convert the range object to a list, with a constructor
return list

'''
def sequence(num):
    result = range(1, num + 1)
    result = list(result)
    return result

print(sequence(5) == [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True

# 7:

'''
input: string
output: string

rules: takes string of a first name, space, last name
returns string of last name, comma, space, first name
names don't include middle names, initials, suffixes

data: string, list

algorithm: split input string using split on the space, into a list, and point it to a variable
return an f-string of list index 1, comma, space, list index 0
'''

def swap_name(s):
    string_list = s.split(' ')
    return f"{string_list[1] + ', ' + string_list[0]}"

print(swap_name('Joe Roberts') == "Roberts, Joe")   # True

# Further exploration:

'''
input: string
output: string

rules: takes string of a first name, middle name(s), last name
returns string of last name, comma, space, first name, space, middle name(s)

data: string, list

algorithm: split input string using split on the space, into a list, and point it to a variable
return an f-string of last list index (-1) and comma 
iterate over the remaining names with for loop
per name, add a space and name to the variable
return variable
'''

def swap_name(s):
    string_list = s.split(' ')
    string_result = f"{string_list[-1] + ','}"
    
    for word in string_list[:-1]:
        string_result += f"{' ' + word}"
        
    return string_result

print(swap_name('Karl Oskar Henriksson Ragvals')
                == "Ragvals, Karl Oskar Henriksson")  # True

# 8:

'''
input: 2 integers
output: list

rules: 
1. 1st arg is a count, 2nd arg is the starting number of a sequence the function makes
2. should return list with same number of elements as 1st arg
3. each element is multiplied by its position in the sequence (not index)
4. count is always 0+. if it's 0, it returns an empty list
5. starting number can be anything

data: integers, lists

algorithm: 
create a 'result_list' variable, empty list
use a for loop to iterate over a range between 1 and count + 1
for each iteration, append to result_list a multiplied starting number with iteration
return result_list
'''

def sequence(count_num, start_num):
    result_list = []
    
    for iteration in range(1, count_num + 1):
        result_list.append(start_num * iteration)
    
    return result_list

print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True

# 9:

'''
input: list
output: list with elements in a reversed order

rules:
1. mutate-reverse the list passed into the function
2. return that reversed list
3. can't use list.reverse or [::-1]

implicit rules:
1. parts of sequence elements are not themselves reversed
2. an empty list input results in an empty list

data: list

algorithm:
1. use a for loop to iterate over the numbers in the input list
2.     in it, create an index integer variable, set to the .index method of number in list
3.     use the .insert method to place the .popped element (from the end) at position of the index variable
4. return list

'''

def reverse_list(lst):
    for num in lst:
        idx = lst.index(num)
        lst.insert(idx, lst.pop())
        
    return lst

list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True

# 10:

'''
input: string
output: boolean

rules:
1. returns True if all parentheses are balanced, False otherwise
2. balanced pairs start with '('
implicit rules:
1. it's not about equal #s of parentheses, it's that they all must be closed
2. no parentheses in string returns True

data: strings, booleans

algorithm:
create an empty 'parentheses' string variable
use a for loop: from the input string, add ( and ) to 'parentheses' string
then check: if there is an equal amount of ( and ), AND it begins with ( AND it ends with ), return True. otherwise return False
'''

def is_balanced(s):
    parentheses = ''
    
    for char in s:
        if char == '(' or char == ')':
            parentheses += char
            
    if parentheses == '':
        return True
    elif parentheses.count('(') == parentheses.count(')') and parentheses[0] == '(' and parentheses[-1] == ')':
        return True
    else:
        return False

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True

'''
input: string
output: boolean

rules:
1. returns True if all marks are balanced and paired, False otherwise

implicit rules:
1. it's not about equal #s of marks, it's that they all must be closed
2. no marks in string returns True

data: strings, lists, booleans

algorithm:
1. create a marks_start list with 3 of the opening marks: (, [, {
2. create a marks_end list with 3 of the closing marks: ), ], }
3. create an open_marks empty list

4. in a for loop, check if each char in input is in marks_start. 
    if it is, append it to open_marks
    
5. then check if each char is in marks_end. 
    if it is, if there is no matching mark in open_marks, or the most recent open mark is not matching, return False
    
6. if the return mark is matching, pop the matching mark (it will be the most recent one) from open_marks

7: a check for (some) apostrophes:
    because of apostrophes and words ending with a single quote mark, we should check whether a single quote mark has an alphabetic character before it
    
8. we initialize a 'not_apostrophes' counter to 0

9. in a for loop of an enumerated string, we check if a character is a '
    if it is, and if it's not the first character, and if the character before it is not a letter, we add 1 to 'not_apostrophes'

10. return three checks at once:
    whether open_marks still has any marks in there (if it is, return False)
    
    plus whether not_apostrophes (so, quote marks (maybe i'm missing an edge case)) is an even amount (if they're not, return False)
    
    plus whether "s in the input were of an even amount (if they're not, return False)
    
---
there are also apostrophes at the beginnings of some words ('til) and nested quotes. the code doesn't yet consider these.
---
'''

def is_balanced(s):
    marks_start = ["(", "[", "{"]
    marks_end = [")", "]", "}"]
    open_marks = []
    
    for char in s:
        if char in marks_start:
            open_marks.append(char)
            
        if char in marks_end:
            if not open_marks or marks_end.index(char) != marks_start.index(open_marks[-1]):
                return False
            
            else:
                open_marks.pop()
                
    not_apostrophes = 0
    
    for idx, char in enumerate(s):
        if char == "'":
            if idx > 0 and s[idx - 1].isalpha():
                continue
            not_apostrophes += 1

    return not open_marks and not_apostrophes % 2 == 0 and s.count('"') % 2 == 0

print(is_balanced("What (is) this?") == True)        # True
print(is_balanced("What is) this?") == False)        # True
print(is_balanced("What (is this?") == False)        # True
print(is_balanced("((What) (is this))?") == True)    # True
print(is_balanced("((What)) (is this))?") == False)  # True
print(is_balanced("Hey!") == True)                   # True
print(is_balanced(")Hey!(") == False)                # True
print(is_balanced("What ((is))) up(") == False)      # True