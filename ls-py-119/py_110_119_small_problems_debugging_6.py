# 1:

'''
Code is not behaving because 'return counter - 1' just returns the expression result, which is 9, but does not update counter. 

But if we were to turn it into a reassignment ("counter -= 1"), the function would no longer be dealing with the globally initialized counter, but instead with the local variable "counter".

Making the smallest possible change, inside the loop we can reassign "counter" to "decrease(counter)" with each iteration, so that counter points to the decrementing return value of "decrease(counter)", from 10 to 1.
'''

def decrease(counter):
    return counter - 1

counter = 10

for _ in range(10):
    print(counter)
    counter = decrease(counter)

print('LAUNCH!')

# 2:

'''
The given code:

for char in string:
    string = char + string
    
is prepending char to string 5 times, but at the end the original string remains behind it, and the result is "ollehhello".

string = string[::-1] will work.
'''

def reverse_string(string):
    string = string[::-1]

    return string

print(reverse_string("hello") == "olleh")

# 3:

'''
Integers are immutable. "item *= 2" is logical, and the function could return the result of that expression, but the results won't be "saved" to the input ingegers. 

The function also has no explicit return.

The following would work (or a comprehension):
'''

def multiply_list(lst):
    result_list = []
    
    for item in lst:
        result_list.append(item * 2)

    return result_list

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# 4:

'''
The code has the wrong syntax for checking a key's presence. "if my_dict[key]:" is accessing a value, not the key.

You can check for a key in 2 ways:
1. if 'key' in my_dict
(this just checks if it's there)

2. if my_dict.get('key')
(this checks if it's there and the value is truthy)

2.5: given solution:
def get_key_value(my_dict, key):
    return my_dict.get(key, None)

So you can correct by writing the following:
'''

def get_key_value(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

# 5:

'''
The code is just checking the opposite of its intention; event days exist in the dictionary, non-event days don't. Corrected version:
'''

events = {
    "2023-08-13": ["Python debugging exercises"],
    "2023-08-14": ["Read 'Automate the Boring Stuff'"],
    "2023-08-15": ["Webinar: Python for Data Science"],
}

def is_date_available(date):
    if date not in events:
        return True

    return False

print(is_date_available("2023-08-14"))  # should return False
print(is_date_available("2023-08-16"))  # should return True

# 6:

'''
default values persist through function calls. the buggy code initializes lst on the first function call, then appends a second integer to it on the second function call.

LS solution is one way to go around this issue, another is:
'''

def append_to_list(value):
    lst = []
    lst.append(value)
    return lst

print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

# 7:

'''
The function name is a built-in function name, 'sum'. On its own it's inadvisable but would be functional, but the function also uses the sum function inside of itself, and 'sum' is now reserved by the function name. So the function tries to use the function again, instead of sum-ming something.

Rename the function to anything else:
'''

def sum_nums(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(sum_nums(numbers, 2) == 20)

# 8:

'''
Because it's a list of lists, when the shallow copy is made, it only copies the outer list, but not the inner lists - they still reference the same objects. To copy those as well, make a deep copy:
'''

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])

# 9:

'''
You can't change the size of a set (or a dictionary) while iterating over it, but a list you can. A set comprehension can both iterate over the original and return values / create a new set:
'''
data_set = {1, 2, 3, 4, 5}
data_set = {item for item in data_set if item % 2 == 0}
print(data_set) # {2, 4}

# 10:

'''
We can preserve the order by skipping the set stuff and checking if the element isn't in unique_data, and append to it if it's not:
'''

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []

for num in data:
    if num not in unique_data:
        unique_data.append(num)
        
print(unique_data)