# 1:

'''
input: dictionary
output: dictionary (inverted)

rules:
1. Given a dict where keys and values are unique, invert it; keys become values, values become keys

data: dictionary

algorithm:
1. create a list of dictionaries from an .items view object of the input dictionary, point it to a variable
2. use a comprehension to iterate over the dictionary items in the list, and return the 2nd item 1st and the 1st item 2nd, for all items
(or the comprehension can just iterate over the view object directly)
'''

def invert_dict(dct):
    dct_items = list(dct.items())
    return {item[1]: item[0] for item in dct_items}

print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True

# 2:

'''
input: dictionary
output: dictionary (of certain pairs)

rules: given a dict and a list of keys, return a dict with k/v pairs for those keys

data: dictionaries, lists

algorithm:
1. return the result of a dict comprehension
2. in the comprehension, return k/v pairs of those keys in the dictionary that are also in the input list of keys
'''

def keep_keys(dct, dct_keys):
    return {key: dct[key] for key in dct if key in dct_keys}

input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

# 3:

'''
input: list
output: list

rules:
1. returns a list of input strings, without the vowels
2. vowels are a, e, i, o, u

examples:
1. if a string is all vowels, the output is an empty string
2. capital vowels are removed too

data: list, string

algorithm:
1. create a VOWELS constant string, with lowercase and uppercase vowels
2. initialize an empty string 'result_string'
3. initialize an empty list 'result_list'
4. in a for loop of string in list, of character in string, add characters to result_string if they're not in VOWELS
5. per string, append that new string to 'result_list'
6. clear result_string by reassigning it to an empty string ''
7. return result_list
'''

def remove_vowels(lst):
    VOWELS = 'AEIOUaeiou'

    result_string = ''
    result_list = []
    
    for s in lst:
        for char in s:
            if char not in VOWELS:
                result_string += char
        result_list.append(result_string)
        result_string = ''
                
    return result_list
    
# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original) == expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True

# 4:

'''
input: string
output: list

rules:
1. returns a list with every word from input string + space + word's length integer
2. if argument is '' or no argument, return empty list
3. every pair of words is separated by 1 space

examples:
1. all punctuation marks attached to words are part of the word in the counting

algorithm:
1. we have a test case where no argument is provided, so to avoid a TypeError, we have to set a default argument. an empty string is the most fitting one
2. now, if an empty string is passed in through the argument or the default argument, we return False immediately
3. otherwise: split the string by the single spaces separating each word and point the return to a 'list_of_strings' variable
4. return the return value of a list comprehension of an f-string of string and length of string, for each string in 'list_of_strings'
'''

def word_lengths(s=''):
    if not s:
        return []
    
    list_of_strings = s.split()
    return [f"{string} {len(string)}" for string in list_of_strings]
    
# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True

# 5:

'''
input: 2 lists of integers of the same length
output: list

rules: 
return a new list with each element the product of corresponding elements from 2 input lists

data: list

algorithm:
1. in a list comprehension, use an index variable of the range of length of either input list
2. use the index variable to iterate over the elements in the lists, and multiply each pair
3. return the return value of the comprehension
'''

def multiply_items(l1, l2):
    
    return [l1[idx] * l2[idx] for idx in range(len(l1))]

list_a = [1, 2, 3]
list_b = [4, 5, 6]
print(multiply_items(list_a, list_b) == [4, 10, 18]) # True

# 6:

'''
input: list of integer(s)
output: integer

rules:
1. function takes a list of number(s), returns sum of sums of subsequences in list
2. input list contains at least 1 number

data: lists, integers

algorithm:
1. in a generator expression, iterate over the index of range of length of list
2. as index is iterating, sum slices from the beginning of the list to index + 1
3. then sum the sums of those together
4. return the final number

Originally I had it as a list comprehension. LSBot review:
"You can drop the square brackets inside sum and use a generator expression instead. This is a common Python style when you’re immediately passing a comprehension to a function like sum, any, or all."

(Brackets are the difference):
def sum_of_sums(lst):
    return sum([sum(lst[0:idx + 1]) for idx in range(len(lst))])
'''

def sum_of_sums(lst):
    return sum(sum(lst[0:idx + 1]) for idx in range(len(lst)))

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True

# 7:

'''
input: integer
output: integer

rules:
1. function takes one positive integer
2. returns the sum of its digits

data: integer, string, maybe list

algorithm:
1. convert input int to string using a constructor and point it to variable

2. in the same line, convert string to list of strings using a constructor

3. use a comprehension + constructor to iterate over the integer version of each string, using an index of range of length of the string

4. sum the list of values that the comprehension generates

A much easier version from LSBot Hints:

def sum_digits(num):
    return sum(int(digit) for digit in str(num))
'''

def sum_digits(num):
    string_nums = list(str(num))
    return sum([int(string_nums[idx]) for idx in range(len(string_nums))])

print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True

# 8:

'''
input: string
output: string

rules:
1. function takes string as arg, returns string with staggered capitalization
2. starting from 1st char, chars should be capitalized
3. followed by a lowercase or a non-alpha char
4. non-alphas should not be changed, but are counted in capitalization system

data: string

algorithm:
1. initialize a 'result_string' empty string
2. make a for loop that iterates through index in the range of the length of the string
3. in the for loop, initialize a 'char' variable and point it to the current index of the string

4. write a nested if statement. if the character's index is even, move to the inner if statement
5. in it, if the character is alphabetic, then add the uppercase version of it to return_string. otherwise, add the character to return_string
6. back in the outer if statement, if the character's index is not even, then add the lowercase version of it to result_string. this won't have an effect on non-alphabetic characters

7. return result_string
'''

def staggered_case(s):
    result_string = ''
    
    for idx in range(len(s)):
        char = s[idx]
        if idx % 2 == 0:
            if char.isalpha():
                result_string += char.upper()
            else: 
                result_string += char
        else:
            result_string += char.lower()
        
    return result_string

string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

# 9:

'''
input: string
output: string

rules:
1. function takes string as arg, returns string with alternated capitalization
2. ignores non-alphabetic characters when alternating the order
3. starting from 1st char, chars should be capitalized, if alphabetical
4. followed by a lowercase or a non-alpha char
5. non-alphas should not be changed, but are included in result string

data: string, integer

algorithm:
1. initialize a 'result_string' empty string
2. initialize a 'counter' variable, set to 0
3. make a for loop that iterates through characters in the input string

4. have an initial if statement: if character is alphabetic, increment counter by 1
5. write a nested if statement: if also the counter is odd, add the upper version of it to 'result_string'
6. else if the counter is even, add the lower version to 'result_string'

7. and back to the outer if statement, if the char is not alphabetic, just add it as is
8. return 'result_string'
'''

def staggered_case(s):
    result_string = ''
    counter = 0
    
    for char in s:
        if char.isalpha():
            counter += 1
            
            if counter % 2 != 0:
                result_string += char.upper()
            else: 
                result_string += char.lower()
                
        else:
            result_string += char
        
    return result_string

string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True

# 10:

'''
input: list (of integers)
output: list (of integer(s))

rules:
1. given a sequence of integers, filter out instances of an integer appearing more than once in a row
2. keep the first instance of any sequence of the same integer
3. return the new sequence, in a list

data: lists, integers

algorithm:
1. initialize a 'result_list' empty list
2. for loop: for el in lst
3.     if statement: if result_list is empty, or if result_list[-1] != el, append el to result_list
4.     no else statement needed, just don't do anything otherwise. at the end of iterating, return result_list

'''
def unique_sequence(lst):
    result_list = []
    for el in lst:
        if not result_list or result_list[-1] != el:
            result_list.append(el)
            
    return result_list

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True

# Non-consecutive duplicates are kept
original = [1, 2, 1, 3]
expected = [1, 2, 1, 3]
print(unique_sequence(original) == expected)      # True

original = []
expected = []
print(unique_sequence(original) == expected)      # True