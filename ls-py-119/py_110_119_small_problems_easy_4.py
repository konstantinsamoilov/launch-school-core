# 1 (Maybe the word for a number should come from its value, not its position, but for this problem I think it works.)
# But also the LS solution is much simpler and better.

'''
input: list
output: list

rules: 1. takes integers between 0-19
2. returns another list of integers 0-19 sorted based on the English word

data: list, integer, string

algorithm:
1. create a list of English words 0-19
2. use zip with the list constructor to make a combined list of tuples, of input list and list of words
3. create a function that takes the combined list and returns the tuple's 2nd element
4. use the function as a key with a sorted() function on combined_list, and point it to a new, sorted combined list
5. create an 'expected_result' empty list
6. use a for loop to iterate over the sorted combined list, and add the 1st element (ints) to expected_result
7. return expected_result
'''

def get_word_element(pair):
    return pair[1]

def alphabetic_number_sort(lst):
    words_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    
    combined_list = list(zip(lst, words_list))
    
    sorted_combined_list = sorted(combined_list, key=get_word_element)
    
    expected_result = []
    
    for tup in sorted_combined_list:
        expected_result.append(tup[0])

    return expected_result

input_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
              10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

expected_result = [8, 18, 11, 15, 5, 4, 14, 9, 19, 1,
                   7, 17, 6, 16, 10, 13, 3, 12, 2, 0]

print(alphabetic_number_sort(input_list) == expected_result) # Prints True

# 2:

'''
input: 2 lists
output: set

rules:
1. convert 2 input lists to sets
2. return a new set that is the union of both sets

data: lists, sets

algorithm:
1. convert both lists to sets using the set constructor, and point them to new variables
2. perform a union on the sets, and either return in the same line, or point the union to another variable and return that
'''

def merge_sets(l1, l2):
    set1 = set(l1)
    set2 = set(l2)
    
    return set1 | set2

list1 = [3, 5, 7, 9]
list2 = [5, 7, 11, 13]
print(merge_sets(list1, list2) == {3, 5, 7, 9, 11, 13}) # Prints True

# LS solution is better:
# def merge_sets(list1, list2):
#     return set(list1) | set(list2)

# 3:

'''
input: 2 lists
output: frozenset

rules: 
1. transform 2 lists into 2 frozen sets
2. find their common elements

data: lists, frozensets

algorithm:
1. transform 2 lists into 2 frozen sets, using constructors
2. use the .intersection (&) method to find the common elements between the two f-sets, and return them
'''

def intersection(l1, l2):
    return frozenset(l1) & frozenset(l2)

list1 = [2, 4, 6, 8]
list2 = [1, 3, 5, 7, 8]
expected_result = frozenset({8})
print(intersection(list1, list2) == expected_result) # True

# 4:

'''
input: dictionary
output: list

rules:
1. given a dictionary, return its keys, in a list
2. the keys should be sorted in the order of the values (2-6-8)

data: dict, list

algorithm:
1. create a list of tuples of the items of the dictionary, point it to variable

2. create a function that returns the second item from each tuple passed into it

3. set that function as the key to a .sort method on the list of tuples

the .sort method will iterate through each tuple and call the function for each tuple

it will assign a key for each tuple, and sort the list of tuples in ascending order of those keys
    
4. create a 'result_keys' empty list

5. in a for loop of tuples in the list of tuples, append each 1st element of each tuple to result_keys

6. return result_keys

'''
def sort_by_int(tup):
    return tup[1]

def order_by_value(d): 
    dict_items = list(d.items())

    dict_items.sort(key=sort_by_int)

    result_keys = []
    
    for tup in dict_items:
        result_keys.append(tup[0])
    return result_keys

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True

# 5:

'''
input: 2 lists
output: set

rules:
1. determine the elements that are unique to list 1
2. return value should be a set

data: list, set

algorithm:
1. convert the lists to sets with constructors
2. perform .difference (-) on the sets, with set(l1) first
3. return the .difference
'''

def unique_from_first(l1, l2):
    return set(l1) - set(l2)

list1 = [3, 6, 9, 12]
list2 = [6, 12, 15, 18]
print(unique_from_first(list1, list2) == {9, 3})

# 6:

'''
input: string
output: list of substrings

rules:
1. takes a string argument. returns a list of substrings of that string
2. each substring should begin with the first letter of the string
3. the list should be ordered from shortest to longest

data: string, list

algorithm:
1. create a 'result_list' empty list
2. create a 'substring' empty string
3. in a for loop of characters in input string, add character to substring
4. and check if substring is in result_list. if it's not, add it
5. return result_list
'''

def leading_substrings(s):
    result_list = []
    substring = ''
    
    for char in s:
        substring += char
        if substring not in result_list:
            result_list.append(substring)
            
    return result_list

# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])

# 7:

'''
input: string
output: list of substings of string, ordered with height and width

rules:
1. Make a function that returns a list of all substrings in a string.
2. Order the columns of the list by where in the string the substring begins.
3. Order the rows by shortest to longest substring.
4. Can use leading_substrings from before.

data: string, list

algorithm:
1. convert the input string to a list using a constructor and point it to 'string_list'

2. create an empty list 'substring_list'

3. in a while loop of string_list, use LS's leading_substrings code as the argument for appending to substring_list

the code iterates over the range of the length of string_list (5 in test case, so 0-1-2-3-4), and appends every substring of the current string_list

first it generates "a", "ab", "abc", "abcd", and "abcde"

4. pop the first item from string_list, so that the next time we can iterate starting at the 2nd character

5. create a 'result_list' empty list

6. in a nested for loop, of the nested lists in substring_list, and of the elements in the nested_lists, append the elements with the .join method, to turn them into strings

7. return result_list
'''

def substrings(s):
    string_list = list(s)
    substring_list = []
    
    while string_list:
        substring_list.append([string_list[:idx + 1] for idx in range(len(string_list))])
        string_list.pop(0)

    result_list = []
        
    for nested_list in substring_list:
        for elements in nested_list:
            result_list.append(''.join(elements))
        
    return result_list
    
expected_result = [
    "a", "ab", "abc", "abcd", "abcde",
    "b", "bc", "bcd", "bcde",
    "c", "cd", "cde",
    "d", "de",
    "e",
]

print(substrings('abcde') == expected_result)  # True

# 8:

'''
input: string
output: list

rules:
1. return a list of all palindromic substrings of a string
2. substrings should be sorted by their order of appearance in input string
3. duplicate substrings should be included multiple times
4. should use LS's 'substrings' from before
5. consider all characters and make it case-sensitive 
    ('AbcbA' is palindrome, 'Abcba' not)
6. single characters are not palindromes

examples:
1. if input string has no palindrome, output is an empty list

data: strings, lists

algorithm:
1. convert string to list using constructor, point to 'string_list' variable
2. create an empty list 'palindrome_element_list'

3. in a while loop of string_list, append to palindrome_element_list, and pass to .append:
elements of all substrings, in lists, for the range of the length of the string, 
of those substrings that are:
equal to themselves when reversed
longer than 1 characters

4. after iterating through all the substrings starting at the 1st index of the string,
pop the 1st element from string_list

5. continue iterating through string_list, until it's empty

6. create a 'result_list' empty list

7. in a for loop of nested lists in palindrome_element_list, in a nested for loop of elements in the nested lists, append to result_list, and pass to append the join method used on elements

8. return result_list
'''

def palindromes(s):
    string_list = list(s)
    palindrome_element_list = []
    
    while string_list:
        palindrome_element_list.append([string_list[:idx + 1]
                               for idx in range(len(string_list))
                               if string_list[:idx + 1] == string_list[:idx + 1][::-1] and len(string_list[:idx + 1]) > 1])
        string_list.pop(0)
        
    result_list = []
        
    for nested_list in palindrome_element_list:
        for elements in nested_list:
            result_list.append(''.join(elements))
        
    return result_list

print(palindromes('abcd') == [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True

# 9:

'''
input: integer, list of dictionaries (variable)
output: list of dictionaries

rules: given an item ID and list of transactions, return list with only transactions for the specified item ID

data: integers, lists, dictionaries

algorithm:
1. in a list comprehension, return those dictionaries in the input list whose value for "id" matches the input value.
2. return the list created by the comprehension.
'''

def transactions_for(id_num, lst):
    
    return [dct for dct in lst if dct["id"] == id_num]

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(transactions_for(101, transactions) ==
      [
          {"id": 101, "movement": "in",  "quantity":  5},
          {"id": 101, "movement": "in",  "quantity": 12},
          {"id": 101, "movement": "out", "quantity": 18},
      ]) # True

# 10:

'''
input: integer, list of dictionaries (variable)
output: boolean

rules:
1. function returns True/False based on whether inventory item is available
2. function takes an item ID and a list of transactions
3. returns True if sum of its quantities in transactions is > 0
4. there are movements in and movements out for the item quantities
5. should use code from previous exercise

questions:
what if the item id passed to the function is not in transactions?

data: integers, lists, dictionaries

algorithm:
1. in a list comprehension, return those dictionaries in the input list whose value for "id" matches the input value. point them to a variable

2. if item passed to function is not in transactions, return False

3. initialize a 'quantity_count' variable, set to 0

4. use a for loop for transactions in the list of transactions. 

while iterating, if the value of a transaction's 'movement' is 'in', add the corresponding 'quantity' to quantity_count

vice versa for 'movement': 'out' -- subtract from quantity_count

5. perform a check - if quantity_count is over 0, return True. otherwise, return False
'''

def is_item_available(id_num, lst):
    id_transactions = [dct for dct in lst if dct["id"] == id_num]
    
    if not id_transactions:
        return False
    
    quantity_count = 0
    
    for transactions in id_transactions:
        if transactions['movement'] == 'in':
            quantity_count += transactions['quantity']
        else:
            quantity_count -= transactions['quantity']
        
    return quantity_count > 0

transactions = [
    {"id": 101, "movement": 'in',  "quantity":  5},
    {"id": 105, "movement": 'in',  "quantity": 10},
    {"id": 102, "movement": 'out', "quantity": 17},
    {"id": 101, "movement": 'in',  "quantity": 12},
    {"id": 103, "movement": 'out', "quantity": 20},
    {"id": 102, "movement": 'out', "quantity": 15},
    {"id": 105, "movement": 'in',  "quantity": 25},
    {"id": 101, "movement": 'out', "quantity": 18},
    {"id": 102, "movement": 'in',  "quantity": 22},
    {"id": 103, "movement": 'out', "quantity": 15},
]

print(is_item_available(101, transactions) == False)  # True
print(is_item_available(103, transactions) == False)  # True
print(is_item_available(105, transactions) == True)   # True