# 9:
"""
PROBLEM:
Given a string, write a function `palindrome_substrings` which returns
all the palindromic substrings of the string that are 2 or more characters
long. Palindrome detection should be case-sensitive.

input: string
output: list of string(s)
rules:
    explicit:
        If a palindromic substring is 2+ characters, it's returned
        Checking for palindromes is case-sensitive
    implicit:
        Return substrings are ordered longest to shortest
        If the string is empty, or there are no palindromes, the return is an empty list
"""
# Test cases: (Comments show expected return values)
# palindrome_substrings("abcddcbA")   # ["bcddcb", "cddc", "dd"]
# palindrome_substrings("palindrome") # []
# palindrome_substrings("")           # []
# palindrome_substrings("repaper")    # ['repaper', 'epape', 'pap']
# palindrome_substrings("supercalifragilisticexpialidocious") # ["ili"]

# 10:

# def sum_even_number_row(row_number):
#     rows = []
#     start_integer = 2
#     for row_length in range(1, row_number + 1):
#         row = create_row(start_integer, row_length)
#         rows.append(row)
#         start_integer = row[-1] + 2
#     return sum(rows[-1])

# def create_row(start_integer, row_length):
#     row = []
#     current_integer = start_integer
#     while len(row) < row_length:
#         row.append(current_integer)
#         current_integer += 2
#     return row

# print(sum_even_number_row(1) == 2)
# print(sum_even_number_row(2) == 10)
# print(sum_even_number_row(4) == 68)

# print(create_row(2, 1) == [2])
# print(create_row(4, 2) == [4, 6])
# print(create_row(8, 3) == [8, 10, 12])

# 11:
"""
You have a number of building blocks that can be used to build a valid structure. 
There are certain rules about what determines a valid structure:

The building blocks are cubes.
The structure is built in layers.
The top layer is a single block.
A block in an upper layer must be supported by four blocks in a lower layer.
A block in a lower layer can support more than one block in an upper layer.
You cannot leave gaps between blocks.

Write a program that, given the number of available blocks,
calculates the number of blocks left over
after building the tallest possible valid structure.


# inputs: integers?
# outputs: integers / blocks left over
# explicit rules:
#     - cubes
#     - structure is in layers
#     - top layer is 1 block
#     - 1 block has to be supported by 4 blocks
#     - 1 block can support 1+ blocks
#     - no gaps between blocks
#     - program builds tallest valid structure with available blocks
#     - program calculates number of blocks left over after building
# implicit rules:
#     - none yet (no test cases yet)
#     *layer number correlates with minimum number of blocks in the layer
#     *number of blocks in a layer is layer number * layer number (side * side)
#     - after test cases: they confirm the explicit rules

# clarifying qs:
#     - what are blocks? other than being cubes. integers?

# data structures:
#     - maybe sets if each integer is unique per layer
#     - maybe lists/nested lists

# algorithm:
# Receive a number of blocks

# Create the 1st layer of 1 (current_layer variable = 1), maybe as a list with integer 1
#     If 0 blocks, then return 0 leftover blocks

# Subtract 1 from the number of blocks given

# Create the 2nd layer of 4 (2*2), maybe as a 2nd list element with integer 4
# (By incrementing current_layer by 1, and multiplying it by itself)
#     If there are <4 remaining blocks, return <4 leftover blocks

# Subtract 4 from remaining number of blocks given
# Create the 3rd layer of 9 (3*3), maybe as a 3rd list element with integer 4
#     If there are <9 remaining blocks, return <9 leftover blocks

# And so on, in a while loop.
"""
# def calculate_leftover_blocks(blocks):
#     current_layer = 1

#     while blocks >= (current_layer * current_layer):
#         blocks = blocks - (current_layer * current_layer)
#         current_layer += 1

#     return blocks

# print(calculate_leftover_blocks(0) == 0)  # True
# print(calculate_leftover_blocks(1) == 0)  # True
# print(calculate_leftover_blocks(2) == 1)  # True
# print(calculate_leftover_blocks(4) == 3)  # True
# print(calculate_leftover_blocks(5) == 0)  # True
# print(calculate_leftover_blocks(6) == 1)  # True
# print(calculate_leftover_blocks(14) == 0) # True

# 12:
"""
# Step 1:
# inputs: list of strings
# outputs: sorted list of strings

# explicit rules: 
# sort list based on highest number of adjacent consonants a string contains
# if 2 strings have the same number of adjacent consonants, return them in the same order
# consonants are adjacent if they're next to each other or with a space in-between
# implicit rules: 
# ...
# questions: 
# sorted highest to lowest?
# case-sensitive or not?
# what about multiple spaces in-between words?
# do strings always have multiple words?
# can strings be empty?
# say a string is all consonants. how is that counted?

# Step 2:
# Test cases clarify that it's highest-to-lowest, but don't concretely answer the rest

# Step 3:
# lists, maybe dict to track counts per word

# Step 4: (not good but this is how it was before coding it up):
# create a consonant_counts_in_string list
# create a vowels list

# iterate through the input list, for loop
    # create a consonants list
    # inside iterate through the string, for loop
        # if char is a consonant, add it to consonants
        # new iteration, keep adding consonants if there are
            # if vowel or not a space, stop
            # count length of consonants. if that integer is >1, add to consonant_counts_in_string

# take highest integer in consonant_counts_in_string and create a dict[string] = integer pair

# order dictionary keys by values if possible
# return dictionary keys in that order
    # not sure how to keep the same order for keys that have the same integer though
"""

# Step 5:
def sort_by_consonant_count(my_list):
    strings_and_highest_counts = {}
    vowels = 'aeiouAEIOU'

    for s in my_list:
        s_processing = s.replace(' ', '')
        consonants = ''
        consonant_counts_in_string = []
        for char in s_processing:
            if char not in vowels and char != ' ':
                consonants += char
            else:
                if len(consonants) > 1:
                    consonant_counts_in_string.append(len(consonants))
                consonants = ''

# lines 19-20 are to capture all the strings ending in consonants;
# without it, the code would go to the next iteration and not add those consonants:
        if len(consonants) > 1:
            consonant_counts_in_string.append(len(consonants))

        if consonant_counts_in_string:
            strings_and_highest_counts[s] = max(consonant_counts_in_string)
        else:
            strings_and_highest_counts[s] = 0

    def sort_key(s):
        return strings_and_highest_counts[s]

    my_list.sort(key=sort_key, reverse=True)

    return my_list

my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']