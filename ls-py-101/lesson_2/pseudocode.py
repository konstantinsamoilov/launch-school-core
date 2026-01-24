# START
# # Given a collection of integers called "numbers"

# SET iterator = 1
# SET savedNumber = value within numbers collection at space 1

# WHILE iterator <= length of numbers
#     SET currentNumber = value within numbers collection at space "iterator"
#     IF currentNumber > savedNumber
#         savedNumber = currentNumber

#     iterator = iterator + 1

# PRINT savedNumber

def find_greatest(numbers):
    iterator = 0
    saved_number = numbers[iterator]

    while iterator < len(numbers):
        current_number = numbers[iterator]
        if current_number > saved_number:
            saved_number = current_number
        if numbers is None: return

        iterator += 1

    return saved_number

###

# A function that returns the sum of two numbers
# (Casual)
# Given two numbers, number1 and number2
# Add and return them
# (Formal)
# FUNCTION sum_func(number1, number2)
    # RETURN number1 + number2
# END

# A function that takes a list of strings, and returns a string that is all those strings concatenated together
# (Casual)
# Given a list of strings
# Create a new empty string that we'll add to
# Add each string into it, keep adding until there's no more, return it
# (Formal)
# FUNCTION concat_func(lst)
    # SET iterator = 0
    # SET concat_string = ''
    # WHILE iterator < length of elements in lst
        # SET concat_string += lst[iterator]
        # iterator = iterator + 1
    # RETURN concat_string

###

# A function that takes a list of integers, and returns a new list with every other element
# from the original list, starting with the first element. For instance:
# every_other([1,4,7,2,5]) # => [1,7,5]
# (Casual)
# Given a list of integers
# Create an iterator that matches the index
# Create a new empty list

# Iterate through the index
# Filter with remainder % 
# Place those into the new list, return it
# (Formal)
# FUNCTION every_other([lst])
    # SET indx = 0
    # SET alt_list = []

    # WHILE indx < length of lst
        # IF indx % 2 == 0
            # APPEND lst[indx] to alt_list

        # SET indx = indx + 1

###

# A function that determines the index of the 3rd occurrence of a given character in a string. 
# For instance, if the given character is 'x' and the string is 'axbxcdxex', the function should return 6
# (the index of the 3rd 'x'). If the given character does not occur at least 3 times, return None.
# (Casual)
# Given a string
# Look for 3rd occurrence of a char in string and return its index
# If the given char doesn't appear at least 3 times, return None
# (Formal)
# FUNCTION third_char_index(str, target_char)
    # SET occurrences_found = 0

    # ITERATE through str 
        # IF char at index 'i' is equal to target_char
            # INCREMENT occurrences_found by 1

            # IF occurrences_found is equal to 3
                # RETURN `i`

    # RETURN None

def find_third_occurrence(str, target_char):
    occurrences_found = 0

    for i in range(len(str)):
        if str[i] == target_char:
            occurrences_found += 1

            if occurrences_found == 3:
                return i
            
    return None

###

# A function that takes two lists of numbers and returns the result of merging the lists. 
# The elements of the first list should become the elements at the even indexes of the returned list, 
# while the elements of the second list should become the elements at the odd indexes. For instance:
merge([1, 2, 3], [4, 5, 6]) # => [1, 4, 2, 5, 3, 6]
# (Casual)
# Given two lists of numbers
# Merge them alternately into one, first list EVEN indexes, second list ODD indexes
# Just append alternately and it'll work
# (Formal)
# FUNCTION alt_merge(lst1, lst2)
    # SET merged_list = []

    # ITERATE through the range of length of lst1 (since there's equal # of elements in lst1 and lst2)
        # APPEND an element from lst1 to merged_list
        # APPEND an element from lst2 to merged_list
    # RETURN merged_list

# so merge([1, 2, 3], [4, 5, 6]) will return [1, 4, 2, 5, 3, 6]

###

# Flowcharts (next assignment) pseudocode:
# START

# SET large_numbers = []
# SET keep_going = True

# WHILE keep_going == True
    # GET "enter a collection"
    # SET collection
    # SET largest_number = SUBPROCESS "extract the largest one from that collection"
    # large_numbers.append(largest_number)
    # GET "enter another collection?"
    # IF "yes"
        # keep_going = True
    # ELSE
        # keep_going = False

# PRINT large_numbers