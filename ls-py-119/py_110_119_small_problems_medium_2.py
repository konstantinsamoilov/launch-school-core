# 1:

'''
rules:
1. take a string, return a dict with 3 properties:
    % of lowercase chars in string
    % of uppercase chars in string
    % of non-letter chars in string
    
2. return %s as strings between '0.00' and '100.00'

3. round values to 2 decimal points

4. string will have at least 1 char

implicit:
1. the dict keys should be named lowercase, uppercase and neither (strings)

input: string
output: dict
also: int

algo:
1. init a l_counter = 0, u_counter = 0, n_counter = 0

2. for-loop over chars in string:
    3. for the type of char it is, add 1 to that counter
        use .islower(), .isupper(), .isalpha()

4. divide each counter by the length of string
    5. multiply each result by 100
    6. point results to l_percent, u_percent, n_percent

7. init 'expected_result' dict

8. create pairs with string keys and percents as values
    9. add values with :.2f floating-point rounding, using f-strings

10. return expected_result
'''

def letter_percentages(s):
    l_counter = 0
    u_counter = 0
    n_counter = 0
    
    for char in s:
        if char.islower():
            l_counter += 1
        elif char.isupper():
            u_counter += 1
        else:
            n_counter += 1
            
    l_percent = (l_counter / len(s)) * 100
    u_percent = (u_counter / len(s)) * 100
    n_percent = (n_counter / len(s)) * 100
    
    expected_result = {}
    
    expected_result['lowercase'] = f'{l_percent:.2f}'
    expected_result['uppercase'] = f'{u_percent:.2f}'
    expected_result['neither'] = f'{n_percent:.2f}'
    
    return expected_result
    
expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)

# 2:

'''
rules:
1. equis: 3 sides same
2. isos: 2 sides same, 1 side diff
3. scals: all diff
4. for a triangle: sum of lengths of 2 shorter sides > length of longest side
5. each side must be > 0
6. return a type of triangle, or 'invalid', based on 3 int arguments

input: 3 ints
output: string

algo:
1. point list of sides to 'sorted_sides'
2. sort sorted_sides

3. cover invalid first. if any 'side' is <= 0 (done through 'if everything about sorted_sides is not true'),
    4. or if the last side in sorted_sides is < the first two, 
        return 'invalid'

5. if all sides are equal, return 'equilateral'

6. if all sides are divergent, return 'scalene'

7. else, return 'isosceles'
'''

def triangle(side1, side2, side3):
    sorted_sides = [side1, side2, side3]
    
    sorted_sides.sort()

    if not all(sorted_sides) or (sorted_sides[2] > sorted_sides[0] + sorted_sides[1]):
        return 'invalid'
    elif side1 == side2 == side3:
        return 'equilateral'
    elif (side1 != side2) and (side2 != side3) and (side1 != side3):
        return 'scalene'
    else:
        return 'isosceles'

print(triangle(3, 3, 3) == "equilateral")  # True
print(triangle(3, 3, 1.5) == "isosceles")  # True
print(triangle(3, 4, 5) == "scalene")      # True
print(triangle(0, 3, 3) == "invalid")      # True
print(triangle(3, 1, 1) == "invalid")      # True

# 3:

'''
rules:
1. right triangle: 1 angle is 90 degrees
2. acute triangle: all angles are < 90
3. obtuse triangle: any angle is > 90
4. invalid triangle: sum is not 180, or an angle is <= 0
5. return one of these
6. angles are integers, no floats
7. arguments are in degrees

input: 3 ints
output: string

algo:
1. point list of degrees to 'degrees'

2. if sum of degrees is not 180, or if the whole of degrees is not truthy, return 'invalid'

3. if any degree is 90 degrees, return 'right'

4. if any degree is > 90 degrees, return 'obtuse'

5. else, return 'acute'
'''

def triangle(d1, d2, d3):
    degrees = [d1, d2, d3]
    
    if sum(degrees) != 180 or not all(degrees):
        return 'invalid'
    elif d1 == 90 or d2 == 90 or d3 == 90:
        return 'right'
    elif d1 > 90 or d2 > 90 or d3 > 90:
        return 'obtuse'
    else:
        return 'acute'

print(triangle(60, 70, 50) == "acute")      # True
print(triangle(30, 90, 60) == "right")      # True
print(triangle(120, 50, 10) == "obtuse")    # True
print(triangle(0, 90, 90) == "invalid")     # True
print(triangle(50, 50, 50) == "invalid")    # True

# 4:

'''
rules:
1. return # of Friday the 13ths in year of argument
2. year will be 1753+
3. Gregorian calendar will remain...

input: int (year)
output: int (#)

algo:
1. import date from datetime
2. init a counter to 0

3. iterate over a range of months
4. for each month, get the day of (year, month, 13)
5. if that day is a Friday, add 1 to counter

6. return counter
'''
import datetime

def friday_the_13ths(year):
    counter = 0
    
    for month in range(1, 13):
        if datetime.date(year, month, 13).weekday() == 4:
            counter += 1
            
    return counter

print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True

# 5:

'''
rules:
1. featured number is odd, a multiple of 7, and with each digit occurring once
2. return the next featured number after input number
3. return error message if no next featured number
4. largest featured number is 9876543201

input: int
output: int, or error

algo:
1. define a helper function, 'unique_digits'
    2. point number variables to 0
    
    3. for-loop over digits in string version of odd, multiple-of-7 nums (potential featured nums)
        4. match/case, if any digit appears, subtract 1 from corresponding number var
        
    5. init 'counts', point to a list of the values of the number variables after the match/case runs
    
    6. if any value in 'counts' is < -1 (we'll use min to check), return False
        7. otherwise True
        
8. in next_featured(input_num):
    9. init a 'increment_from', point to 0
    10. for-loop over nums in range of input_num + 1 to the last featured num:
        11. if num is odd and a multiple of 7, point increment_from to num
        12. break the loop
        
    13. if increment_from is not the default 0:
        14. for-loop over nums starting at increment_from, to last featured number, steps of 14:
            15. if the call to unique_digits with num is True, return num
            
    16. outside of the second loop, if a featured number is not found, return error     
'''

error = ("There is no possible number that fulfills those requirements.")

def unique_digits(featured):
    zero = one = two = three = four = five = six = seven = eight = nine = 0
    
    for digit in str(featured):
        match digit:
            case '0': zero -= 1
            case '1': one -= 1
            case '2': two -= 1
            case '3': three -= 1
            case '4': four -= 1
            case '5': five -= 1
            case '6': six -= 1
            case '7': seven -= 1
            case '8': eight -= 1
            case '9': nine -= 1
            
    counts = [zero, one, two, three, four, five, six, seven, eight, nine]
            
    if min(counts) < -1:
        return False
    return True

def next_featured(input_num):
    increment_from = 0

    for num in range(input_num + 1, 9876543202):
        if num % 2 != 0 and num % 7 == 0:
            increment_from = num
            break

    if increment_from:
        for num in range(increment_from, 9876543202, 14):
            if unique_digits(num):
                return num
        
    return error

print(next_featured(12) == 21)                  # True
print(next_featured(20) == 21)                  # True
print(next_featured(21) == 35)                  # True
print(next_featured(997) == 1029)               # True
print(next_featured(1029) == 1043)              # True
print(next_featured(999999) == 1023547)         # True
print(next_featured(999999987) == 1023456987)   # True
print(next_featured(9876543186) == 9876543201)  # True
print(next_featured(9876543200) == 9876543201)  # True
print(next_featured(9876543201) == error)       # True

# 6:

'''
rules:
1. compute the diff between:
    2. the square of the sum of positive integers from 1 to input
        (1 + 2 + 3)**2
    3. the sum of the squares of positive integers from 1 to input
        (1**2 + 2**2 + 3**2)
        
input: int
output: int

rules:
1. initialize sum_nums = 0
2. for-loop for square of sum, over num in range(1, input_num + 1):
    3. add each num to sum_nums
4. point 'square_of_sum' to square of sum_nums

5. initialize 'sum_of_squares' = 0
6. for-loop for sum of squares, over num in range(1, input_num + 1)
    7. add to sum_of_squares the square of each num
    
8. return square_of_sum - sum_of_squares
'''
def sum_square_difference(input_num):
    sum_nums = 0
    for num in range(1, input_num + 1):
        sum_nums += num
    square_of_sum = sum_nums**2
    
    sum_of_squares = 0
    for num in range(1, input_num + 1):
        sum_of_squares += num**2

    return square_of_sum - sum_of_squares

print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True

# 7:

'''
rules:
1. bubble sort the input list, in-place
2. list will have at least 2 elements

implicit:
1. strings are sorted alphabetically, numbers in ascending order
2. input list will have either all integers or strings

input: list
output: list

algo:
1. create a 'should_we_sort' function that also takes the input list
    2. in it, for-loop over index in range(1, len(input_list))
        3. if, at any comparison, input_list[idx - 1] is greater than input_list[idx],
           return True (and sort it in the main function)
    4. otherwise return False
    
5. init a 'swapping' global variable, set to ''

6. in 'bubble_sort' function, while should_we_sort is True:
    7. for-loop over index in range(1, len(input_list)):
        8. if, at any comparison, input_list[idx - 1] is greater than input_list[idx],
           (we know there will be, now we're looking for which)
           9. point 'swapping' to input_list[idx - 1]
           10. point input_list[idx - 1] to input_list[idx]
           11. point input_list[idx] to 'swapping'     
'''

def should_we_sort(input_list):
    for idx in range(1, len(input_list)):   
        if input_list[idx - 1] > input_list[idx]:      
            return True
    return False

swapping = ''

def bubble_sort(input_list):
    while should_we_sort(input_list):
        for idx in range(1, len(input_list)):
            if input_list[idx - 1] > input_list[idx]:
                swapping = input_list[idx - 1]
                input_list[idx - 1] = input_list[idx]
                input_list[idx] = swapping

lst1 = [5, 3]
bubble_sort(lst1)
print(lst1 == [3, 5])                   # True

lst2 = [6, 2, 7, 1, 4]
bubble_sort(lst2)
print(lst2 == [1, 2, 4, 6, 7])          # True

lst3 = ['Sue', 'Pete', 'Alice', 'Tyler', 'Rachel',
        'Kim', 'Bonnie']
bubble_sort(lst3)

expected = ["Alice", "Bonnie", "Kim", "Pete",
            "Rachel", "Sue", "Tyler"]
print(lst3 == expected)                 # True