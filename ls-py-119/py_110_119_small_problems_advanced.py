# 1:

'''
rules:
1. return a transpose of input matrix. do not modify input matrix
2. in a 3x3 transpose, row 1 becomes column 1, vice versa, etc
    row 1 <-> column 1
    row 2 <-> column 2
    row 3 <-> column 3
3. no external libraries

input: nested (2-d) list
output: another nested list

algo:
1. point 'row1' to a list with values of input_matrix[0][0], input_matrix[1][0], input_matrix[2][0]
2. point 'row2' to a list with values of input_matrix[0][1], input_matrix[1][1], input_matrix[2][1]
3. point 'row3' to a list with values of input_matrix[0][2], input_matrix[1][2], input_matrix[2][2]

4. point 'transposed_matrix' to a nested list with the 3 rows and return (or just return)
'''

def transpose(input_matrix):
    row1 = [input_matrix[0][0], input_matrix[1][0], input_matrix[2][0]]
    row2 = [input_matrix[0][1], input_matrix[1][1], input_matrix[2][1]]
    row3 = [input_matrix[0][2], input_matrix[1][2], input_matrix[2][2]]
    
    return [row1, row2, row3]

matrix = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

new_matrix = transpose(matrix)

print(new_matrix == [[1, 4, 3], [5, 7, 9], [8, 2, 6]]) # True
print(matrix == [[1, 5, 8], [4, 7, 2], [3, 9, 6]])     # True

# 2:

'''
rules:
1. return a transpose of input matrix. do not modify input matrix
2. matrix can be any shape and size
3. matrix will have at least 1 row and 1 column
4. no external libraries, i assume

input: nested (2-d) list
output: another nested list

algo (before i learned the dark truth of this solution):
notes 1. in a matrix, every time a new sub-list begins, that's another row
notes 2. so we can store the count of elements total, and the count of rows total
notes 3. then transpose via those counts
notes 4. so the following if/elif works for matrices that are either 1 row or 1 column; totally unnecessary to program specifically for those, but i wanted to see what it would look like

1. init a 'row_counter' = 0
2. init a 'el_counter' = 0

3. for sub-list in input list:
    4. add 1 to row_counter
    5. for el in sub-list:
        6. add 1 to el_counter
        
7. init empty list 'result'
8. floor-divide el_counter by row_counter, point to new_row_counter
        
9. if row_counter is 1, then:
    10. result = [[el] for el in input list[0]] (creating rows)
11. elif row_counter equal to el_counter:
    12. result = [[el for sublist in input list for el in sublist]] (creating 1 row)
    
13. else, we're dealing with all other kinds of matrices:
    14. for-loop to make rows in the transposed matrix, over _ in range of new_row_counter
        15. append an empty list/row [] to 'result' that # of times
        
    16. for-loop for row index over range of length of input matrix
        17. inner for-loop for column index over range of outer for-loop
            18. populate result with append, completing row by row (thru col_idx)
            
    19. return result
'''

def transpose(inputmx):
    row_counter = 0
    el_counter = 0
    
    for sublist in inputmx:
        row_counter += 1
        for el in sublist:
            el_counter += 1
            
    result = []
    new_row_counter = el_counter // row_counter
    
    if row_counter == 1:
        result = [[el] for el in inputmx[0]]
    elif row_counter == el_counter:
        result = [[el for sublist in inputmx for el in sublist]]
    else:
        for _ in range(new_row_counter):
            result.append([])

        for row_idx in range(len(inputmx)):
            for col_idx in range(len(inputmx[row_idx])):
                result[col_idx].append(inputmx[row_idx][col_idx])

    return result

# All of these examples should print True
print(transpose([[1, 2, 3, 4]]) == [[1], [2], [3], [4]])
print(transpose([[1], [2], [3], [4]]) == [[1, 2, 3, 4]])
print(transpose([[1]]) == [[1]])

matrix_3_by_5 = [
    [1, 2, 3, 4, 5],
    [4, 3, 2, 1, 0],
    [3, 7, 8, 6, 2],
]
expected_result = [
    [1, 4, 3],
    [2, 3, 7],
    [3, 2, 8],
    [4, 1, 6],
    [5, 0, 2],
]

print(transpose(matrix_3_by_5) == expected_result)

# 3:

'''
rules:
1. take a CxR matrix, rotate it clockwise by 90 degrees, return new rotated matrix
2. don't mutate original matrix

input: list of lists
output: list of lists

algo:
1. count rows and columns in input matrix
    point new_rows to the length of one row / the number of columns
    point new_columns to the length of matrix / number of rows
    
2. create the frame for the 90-degree flipped matrix
    point result to empty list
    for ops in range of new_rows, append nested lists
    
3. each row in the frame needs elements from each column in input matrix, bottom to top
    the code for transposing works to place it in a flipped position
        with just reversal of elements per row needed
    because all these matrices are rectangular, not jagged, we'll simplify the range of the inner loop to 'range(new_rows)'
    
4. for each transposed row, reverse the row
5. return result
'''

def rotate90(mx):
    new_rows = len(mx[0])
    new_columns = len(mx)

    result = []
    
    for _ in range(new_rows):
        result.append([])   
            
    for row_index in range(new_columns):
        for column_index in range(new_rows):
	        result[column_index].append(mx[row_index][column_index])
            
    for row in result:
        row.reverse()

    return result

matrix1 = [
    [1, 5, 8],
    [4, 7, 2],
    [3, 9, 6],
]

matrix2 = [
    [3, 7, 4, 2],
    [5, 1, 0, 8],
]

new_matrix1 = rotate90(matrix1)
new_matrix2 = rotate90(matrix2)
new_matrix3 = rotate90(rotate90(rotate90(rotate90(matrix2))))

# These examples should all print True
print(new_matrix1 == [[3, 4, 1], [9, 7, 5], [6, 2, 8]])
print(new_matrix2 == [[5, 3], [1, 7], [0, 4], [8, 2]])
print(new_matrix3 == matrix2)

# 4:
# Solution with merging the input lists:
'''
rules:
1. take 2 sorted lists, return new list with all elements in ascending order
2. both lists have all integers or all strings
3. build result list 1 element at a time; can't use .sort/sorted
4. don't mutate input lists

input: 2 sorted lists
output: 1 sorted list

algo:
1. LSBot says that we're allowed to use "min()", so:
2. add the input lists and point to 'merged'
3. init 'result' empty list

4. while 'merged':
    5. for index in range of length of 'merged':
        6. if merged[idx] is the smallest value in 'merged':
            7. append it to 'result'
            8. point the element at that index to 'None', instead
            9. break from this for-loop
            
    10. and start another, also for index in range of length of 'merged':
        11. when it finds an element 'None' in 'merged', it pops it
            12. break from this for-loop and go back to the first one
            
13. continue until 'merged' is empty
14. return 'result'
'''

def merge(l1, l2):
    merged = l1 + l2
    result = []
    
    while merged:
        for idx in range(len(merged)):
            if merged[idx] == min(merged):
                result.append(merged[idx])
                merged[idx] = None
                break
        
        for idx in range(len(merged)):
            if merged[idx] == None:
                merged.pop(idx)
                break
                
    return result

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)

# -----
# Solution with keeping input lists (and their copies) separate:
'''
algo:
import copy
init 'result' empty list
copy list1 and list2, point to variables l3 and l4

while-loop: while length of result is smaller than length of names1 + names2
    if both are not empty
        append the minimal el from both to result
    if one is empty
        append the minimal el from the other one to result
        
    if-statement, if both l3 and l4 are not empty, then:
        if the minimal el from both is in l3:
            remove that el from l3
        if it's in l4:
            remove it from l4
    elif l4 is empty:
        remove minimal el from l3
    elif l3 is empty:
        remove minimal el from l4
            
   then it goes back up, and so on
   
   return result
'''

import copy

def merge(l1, l2):
    result = []
    l3 = copy.copy(l1)
    l4 = copy.copy(l2)
    
    while len(result) < len(l1) + len(l2):
        if l3 and l4:
            result.append(min(min(l3), min(l4)))
        elif l3 and not l4:
            result.append(min(l3))
        elif not l3 and l4:
            result.append(min(l4))
                 
        if l3 and l4:     
            if min(min(l3), min(l4)) in l3:
                l3.remove(min(min(l3), min(l4)))
            elif min(min(l3), min(l4)) in l4:
                l4.remove(min(min(l3), min(l4)))
        elif l3 and not l4:
            l3.remove(min(l3))
        elif not l3 and l4:
            l4.remove(min(l4))
                          
    return result

# All of these examples should print True
print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])

names1 = ['Alice', 'Kim', 'Pete', 'Sue']
names2 = ['Bonnie', 'Rachel', 'Tyler']
names_expected = ['Alice', 'Bonnie', 'Kim', 'Pete',
                  'Rachel', 'Sue', 'Tyler']
print(merge(names1, names2) == names_expected)

# 6:

'''
rules:
1. take list, return new list sorted using merge sort
2. input list will be either all numbers or all strings
3. can use merge function from previous exercise
4. input list /can/ be mutated

input: list
output: list

algo:
(I tried splitting without sorting and, though there is a way, it is much more labored.)

Let's explain what happens with print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7]):

import copy for merge function
define my merge function from previous exercise, then merge sort function
merge_sort splits input list into [6, 2] and [7, 1, 4].
then it splits [6, 2] into [6] and [2].

at this point, merge_sort has two frames:
in the 1st, 'lst' points to [6, 2, 7, 1, 4], sublist1 to [6, 2], sublist2 to [7, 1, 4].
in the 2nd, 'lst' points to [6, 2], sublist1 to [6], sublist2 to [2].

it continues executing "sublist1 = merge_sort(sublist1)", thus creating a 3rd frame, where lst points to [6].

because len(lst) == 1, it returns [6], which replaces the function call that just happened, 'merge_sort(sublist1)', reasserting that sublist1 = [6].

it does the same with 'sublist2 = merge_sort(sublist2)'

returning lst both times allows the program to execute below that, which is a 'return merge(sublist1, sublist2)' function call.

'merge' returns a sorted list, from the two sublists it gets (in this program, all the sublists 'merge' gets, except for the final call, will be length 1).

'merge_sort' then returns that result, [2, 6], to sublist1.

    (without a 'return' there, that merge_sort frame just ends. then execution goes to     the higher frame, where lst -> [6, 2, 7, 1, 4], sublist1 -> None, sublist2 -> [7,       1, 4].)

    (from there, it operates on [7, 1, 4], and at the end of that, [1, 4] is also not        returned, and a 2nd, lower frame is now lst -> [7, 1, 4], sublist1 -> [7], sublist      -> None. Then 'merge' fails to find length of NoneType.)

then sublist2 operations begin.

then they are resolved, and the highest frame, sublist1 -> [2, 6], sublist2 -> [1, 4, 7], executes in 'merge'. it returns [1, 2, 4, 6, 7], and 'merge_sort' immediately returns [1, 2, 4, 6, 7] to the user.
'''

import copy

def merge(l1, l2):
    result = []
    l3 = copy.copy(l1)
    l4 = copy.copy(l2)
    
    while len(result) < len(l1) + len(l2):
        if l3 and l4:
            result.append(min(min(l3), min(l4)))
        elif l3 and not l4:
            result.append(min(l3))
        elif not l3 and l4:
            result.append(min(l4))
                 
        if l3 and l4:     
            if min(min(l3), min(l4)) in l3:
                l3.remove(min(min(l3), min(l4)))
            elif min(min(l3), min(l4)) in l4:
                l4.remove(min(min(l3), min(l4)))
        elif l3 and not l4:
            l3.remove(min(l3))
        elif not l3 and l4:
            l4.remove(min(l4))
                          
    return result

def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    sublist1 = lst[:len(lst) // 2]
    sublist2 = lst[len(lst) // 2:]
    
    sublist1 = merge_sort(sublist1)
    sublist2 = merge_sort(sublist2)
    
    return merge(sublist1, sublist2)

# All of these examples should print True
print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([9, 2, 7, 6, 8, 5, 0, 1]) == [0, 1, 2, 5, 6, 7, 8, 9])

original = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
            'Kim', 'Bonnie']
expected = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel',
            'Sue', 'Tyler']
print(merge_sort(original) == expected)

original = [7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54,
            43, 5, 25, 35, 18, 46]
expected = [1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25,
            35, 37, 43, 46, 51, 54]
print(merge_sort(original) == expected)

# 7:

'''
rules:
1. implement binary search
2. take a list and search item, return index of search item, if found
3. if not found, return -1
4. the list argument will always be sorted

input: list, search item from list (str/int)
output: int (index)

algo:
init 'offset' variable, point to 0

while-loop on lst:
    floor-divide length of lst, point to 'middle_index'

if value at list middle index is same as search item,
    return middle index + offset
    
else-if value at list middle index is smaller,
    add middle_index + 1 (the new starting point for lst) to offset
    point lst to lst slice starting at middle_index + 1

else-if value at list middle index is larger,
    we don't need to offset because the indexing in the sliced list will be the same
    point lst to slice ending at middle_index (so, not including it)
    
the program continues to do this, until it finds search_item, or not. if not,
return -1

(lst can become empty when reassigned by lst = lst[middle_index + 1:] or lst = lst[:middle_index] to an empty list.)
'''

def binary_search(lst, search_item):
    offset = 0
    
    while lst:
        middle_index = len(lst) // 2
    
        if lst[middle_index] == search_item:
            return middle_index + offset
        
        elif lst[middle_index] < search_item:
            offset += middle_index + 1
            lst = lst[middle_index + 1:]
            
        elif lst[middle_index] > search_item:
            lst = lst[:middle_index]
            
    return -1

# All of these examples should print True
businesses = ['Apple Store', 'Bags Galore', 'Bike Store',
              'Donuts R Us', 'Eat a Lot', 'Good Food',
              'Pasta Place', 'Pizzeria', 'Tiki Lounge',
              'Zooper']
print(binary_search(businesses, 'Pizzeria') == 7)
print(binary_search(businesses, 'Apple Store') == 0)

print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 77) == -1)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 89) == 6)
print(binary_search([1, 5, 7, 11, 23, 65, 89, 102], 5) == 1)

names = ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue',
         'Tyler']
print(binary_search(names, 'Peter') == -1)
print(binary_search(names, 'Tyler') == 6)

# 8:

'''
rules:
1. function one: take a rational number as arg, return list of denominators that are part of an Egyptian Fraction representation of it (all unit fractions)

2. function two: take a list of denominators of Egyptian unit fractions, return the resulting rational number

3. need to use Fraction class from fractions module

4. the output of 'egyptian' can be reversed by 'unegyptian'

5. every rational number can be expressed as an Egyptian Fraction in infinite ways, so my results may be different from this solution

'egyptian':
input: 2 ints (rational number)
output: list of ints (denominators)

algo:
from fractions import Fraction
init 'iterating_denominator', point to 1
init 'denominator_list' empty list

while-loop for the fraction number argument:
    if fraction_arg is larger or equal to fraction number of 1, iterating_denominator:
        subtract that from fraction_arg
        then append the .denominator part of the Fraction number to denominator_list
        
    in all cases, increment iterating_denominator by 1, to continue trying to subtract
    
when fraction_arg is fully subtracted from and we have all the denominators that did it, return denominator_list
'''

from fractions import Fraction

def egyptian(fraction_arg):
    iterating_denominator = 1
    denominator_list = []
    
    while fraction_arg:
        if fraction_arg >= Fraction(1, iterating_denominator):
            fraction_arg -= Fraction(1, iterating_denominator)
            denominator_list.append(Fraction(1, iterating_denominator).denominator)
            
        iterating_denominator += 1
        
    return denominator_list

'''
'unegyptian':
input: list (of denominators)
output: Fraction number (2 ints)

algo:
init 'egyptian_fraction_sum', point to 0

for-loop for number in denominator_list,
    add the Fraction number of 1 / number from denominator_list to 'egyptian_fraction_sum'

return the Fraction number of egyptian_fraction_sum
'''

def unegyptian(denominator_list):
    egyptian_fraction_sum = 0
    
    for num in denominator_list:
        egyptian_fraction_sum += Fraction(1, num)
        
    return Fraction(egyptian_fraction_sum)
    
# Using the egyptian function
# Your results may differ for these first 3 examples
print(egyptian(Fraction(2, 1)))      # [1, 2, 3, 6]
print(egyptian(Fraction(137, 60)))   # [1, 2, 3, 4, 5]
print(egyptian(Fraction(3, 1)))
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 230, 57960]

# Using the unegyptian function
# All of these examples should print True
print(unegyptian(egyptian(Fraction(1, 2))) == Fraction(1, 2))
print(unegyptian(egyptian(Fraction(3, 4))) == Fraction(3, 4))
print(unegyptian(egyptian(Fraction(39, 20))) == Fraction(39, 20))
print(unegyptian(egyptian(Fraction(127, 130))) == Fraction(127, 130))
print(unegyptian(egyptian(Fraction(5, 7))) == Fraction(5, 7))
print(unegyptian(egyptian(Fraction(1, 1))) == Fraction(1, 1))
print(unegyptian(egyptian(Fraction(2, 1))) == Fraction(2, 1))
print(unegyptian(egyptian(Fraction(3, 1))) == Fraction(3, 1))