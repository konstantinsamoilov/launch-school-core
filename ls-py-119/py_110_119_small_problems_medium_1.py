# 1:

'''
rules:
1. rotate input list by moving 1st el to end
2. don't modify input list; return new list
3. if input is [], return []
4. if input is not list, return None

input: list
output: list
also: string, dict, ...

algo:
1. import copy
2.     if input list is not list type, return None
3.     else-if input list is empty list, return []

4.     else: deepcopy input list, point to 'result_list'
5.     pop first item, point to 'popped'
6.     append 'popped' to last position

7. return 'result_list'
'''
import copy

def rotate_list(lst):
    if not type(lst) == list:
        return None
    elif lst == []:
        return []
    else:
        result_list = copy.deepcopy(lst)
        popped = result_list.pop(0)
        result_list.append(popped)
    
        return result_list

# All of these examples should print True
print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None) == None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])

# 2:

'''
rules:
1. rotate last digits in input num by the input count
2. move the count-index digit, counting from the right, to the right
3. move the digits it goes over one spot left

input: 2 integers
output: integer
also: string, maybe list

algo:
1. convert num to list of strings, point it to a 'list_of_strings'
2. pop the first digit with -count index, point to 'popped'
3. append 'popped' to the end
4. .join elements, point to 'result_string'
5. convert 'result_string' int, point to 'result_int'
6. return 'result_int'
'''
def rotate_rightmost_digits(num, count):
    list_of_strings = list(str(num))
    
    popped = list_of_strings.pop(-count)
    list_of_strings.append(popped)
    
    result_string = ''.join(list_of_strings)
    
    result_int = int(result_string)
    
    return result_int

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

# 3:

'''
rules:
1. maximally rotate input number and return it
2. can use code from prev exercise

implicit:
1. output for single-digit number it itself
2. leading 0 is dropped when result starts with 0

algo:
1. convert num to list of strings, point to 'list_of_strings'
2. for index of range of length of list:
    3. pop element at index, point to 'popped'
    4. append to list (last element should get popped and appended in same place)
5. convert to string with .join, point to 'result'
6. return int version of 'result'
'''

def max_rotation(num):
    list_of_strings = list(str(num))
    
    for idx in range(len(list_of_strings)):
        popped = list_of_strings.pop(idx)
        list_of_strings.append(popped)
        
    result = ''.join(list_of_strings)
    
    return int(result)

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# Note that the final sequence here is `015`. The leading
# zero gets dropped, though, since we're working with
# an integer.
print(max_rotation(105) == 15)                 # True

# 4:

'''
rules:
1. follow the string arguments and have correct output
2. create all mentioned commands in the function
3. initialize stack to [] and register to 0
4. all programs will be valid
5. all operations are integer operations

input: string
output: integer / nothing

algo:
1. if an integer appears in string, it's the current integer / in the register
    1.5. so it's 'current_value', but must be int
    
2. create a 'stack' empty list
3. create a 'current_value' 0

4. split input string on spaces, point to 'order_of_operations'

5. if element in 'order' is digit, or the first char of el is '-':
    point current_value to integer version of digit

6. else (it's alphabetical):
    match el:
        case 'PUSH': append current_value to stack
        etc this way:
'func_ADD': pop from stack & add to current_value
'func_SUB': pop from stack, sub from current_value, result to current_value
'func_MULT': pop from stack, mult by current_value, result to current_value
'func_DIV': pop from stack, div current_value by popped, int result to current_value
'func_REMAINDER': pop from stack, div current_value by popped, int remainder to current_value
'func_POP': pop from stack, popped to current_value
'func_PRINT': print current_value

7. (Further Exploration):
create case groupings for return error messages if current_value is falsy or if stack is falsy

8. create 'every other case' case, return "Invalid token." for those
'''

def minilang(program):
    stack = []
    current_value = 0
    
    order_of_operations = program.split(' ')
    
    for el in order_of_operations:
        if el.isdigit() or el[0] == '-':
            current_value = int(el)
        else:
            match el:
                case ('PUSH' | 'PRINT') if not current_value:
                    return "No value in register."
                case ('ADD' | 'SUB' | 'MULT' | 'DIV' | 'REMAINDER' | 'POP') if not stack:
                    return "Stack is empty."
                
                case 'PUSH': stack.append(current_value)
                case 'ADD': current_value += stack.pop()  
                case 'SUB': current_value -= stack.pop()
                case 'MULT': current_value *= stack.pop()
                case 'DIV': current_value //= stack.pop()
                case 'REMAINDER': current_value %= stack.pop() 
                case 'POP': current_value = stack.pop()
                case 'PRINT': print(current_value)
                case _: return "Invalid token."

minilang('PRINT')
# 0
print('---')

minilang('5 PUSH 3 MULT PRINT')
# 15
print('---')

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8
print('---')

minilang('5 PUSH POP PRINT')
# 5
print('---')

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7
print('---')

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6
print('---')

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12
print('---')

minilang('-3 PUSH 5 SUB PRINT')
# 8
print('---')

minilang('6 PUSH')
# (nothing is printed)

# 5:

'''
rules:
1. return input string with every "number word" a string digit
2. string won't have punctuation
3. i guess we're only doing zero to nine?

input: string
output: string
also: list

algo:
1. split input string at spaces, point to 'list_of_words'
2. for index and word in enumerated list_of_words:
    3. match lowercase version of word:
        4. case for each number word:
            5. list_of_strings[index] = string digit
        6. case _:
            7. pass
            
8. join list_of_strings, point to 'result'
9. return 'result'
'''
import string
print(string.punctuation)

def word_to_digit(s):
    list_of_words = s.split(' ')
    
    for idx, word in enumerate(list_of_words):
        match word.lower():
            case 'zero': list_of_words[idx] = '0'
            case 'one': list_of_words[idx] = '1'
            case 'two': list_of_words[idx] = '2'
            case 'three': list_of_words[idx] = '3'
            case 'four': list_of_words[idx] = '4'
            case 'five': list_of_words[idx] = '5'
            case 'six': list_of_words[idx] = '6'
            case 'seven': list_of_words[idx] = '7'
            case 'eight': list_of_words[idx] = '8'
            case 'nine': list_of_words[idx] = '9'
        
    result = ' '.join(list_of_words)
    return result

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

# Further exploration:

'''
rules:
1. return input string with every "number word" a string digit
2. string does have punctuation
3. only doing zero to nine for number words

input: string
output: string
also: list

algo:
1. split input string at spaces, point to 'list_of_words'
2. for index and word in enumerated list_of_words:
    3. strip punctuation from ends of word, point to 'clean_word'
    4. create 'digit' empty string
            5. match/case for lowercase version of clean_word:
                6. case (num): digit = (num)
            7. if there is a digit, replace the "clean" part of the current word in list_of_words with the digit part (this preserves the punctuation)    
8. join list_of_strings, point to 'result'
9. return 'result'
'''

import string

def word_to_digit(s):
    list_of_words = s.split(' ')
    
    for idx, word in enumerate(list_of_words):
        clean_word = word.strip(string.punctuation)
        digit = ''
        match clean_word.lower():
            case 'zero': digit = '0'
            case 'one': digit = '1'
            case 'two': digit = '2'
            case 'three': digit = '3'
            case 'four': digit = '4'
            case 'five': digit = '5'
            case 'six': digit = '6'
            case 'seven': digit = '7'
            case 'eight': digit = '8'
            case 'nine': digit = '9'
            
        if digit:
            list_of_words[idx] = word.replace(clean_word, digit)
        
    result = ' '.join(list_of_words)
    return result

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True

# 6:

'''
rules:
1. prime number: divisible only by itself and 1
2. return True if input num is prime, False otherwise
3. can't use any add-on packages

input: int
output: boolean
also: ...

algo:
1. for num in range(2, input_num)
    2. if the remainder of dividing input_num by num is 0 at any point, return False
3. at the end of the loop, if it's never 0, return True
'''

def is_prime(input_num):
    
    if input_num == 1:
        return False

    for num in range(2, input_num):
        if input_num % num == 0:
            return False
    return True

print(is_prime(1) == False)              # True
print(is_prime(2) == True)               # True
print(is_prime(3) == True)               # True
print(is_prime(4) == False)              # True
print(is_prime(5) == True)               # True
print(is_prime(6) == False)              # True
print(is_prime(7) == True)               # True
print(is_prime(8) == False)              # True
print(is_prime(9) == False)              # True
print(is_prime(10) == False)             # True
print(is_prime(23) == True)              # True
print(is_prime(24) == False)             # True
print(is_prime(997) == True)             # True
print(is_prime(998) == False)            # True
print(is_prime(3_297_061) == True)       # True
print(is_prime(23_297_061) == False)     # True

# 7:

'''
rules:
1. fibonacci: each num is sum of previous 2 nums
2. write function that finds the Nth Fibonacci number; N is the argument
3. numbers go: 1, 1, 2, 3, 5, 8, 13, 21, 34

input: int
output: int
also: range

algo:
1. initialize 'first', 'second', to 1, 1
2. if num is 1, return 'first', if num is 2, return 'second'

3. for operations in range(2, num)
    4. add first to second, point to 'result'
    5. point 'first' to 'second'
    6. point 'second' to 'result'
    
7. return 'result'
'''

def fibonacci(num):
    first = 1
    second = 1
    result = 0
    
    if num == 1:
        return first
    if num == 2:
        return second
    
    for operations in range(2, num):
        result = first + second
        first = second
        second = result
        
    return result

print(fibonacci(1) == 1)                  # True
print(fibonacci(2) == 1)                  # True
print(fibonacci(3) == 2)                  # True
print(fibonacci(4) == 3)                  # True
print(fibonacci(5) == 5)                  # True
print(fibonacci(6) == 8)                  # True
print(fibonacci(12) == 144)               # True
print(fibonacci(20) == 6765)              # True
print(fibonacci(50) == 12586269025)       # True
print(fibonacci(75) == 2111485077978050)  # True

# 8:

'''
rules:
1. write a recursive function that computes the Nth Fibonacci number (N is arg)

input: int
output: int

algo:
1. let's take fib(5):
2.     first, if num is equal to or less than 2, return 1

3.     return fib(5 - 1) + fib(5 - 2)
4.     this calls fib(4), which fully resolves before fib(3) is called on the same line
5.         fib(4) then calls fib(3) and fib(2)
6.             fib(3) calls fib(2) and fib(1)
7.                both of those return 1 to fib(3), which adds them and returns 2 to fib(4)

8. and the other trees resolve similarly
'''

def fibonacci(n):
    if n <= 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True

# 9:

'''
rules:
1. create memoization for the previous code

input: int
output: int

algo:
1. because recursion first completes one entire branch (i.e. when two function calls happen inside a function, the first one is resolved completely before the second one is called), we are able to track the return values and save them

2. and then reuse them for everything that has been computed thus far

3. define an empty dictionary outside of the function

4. create an if/elif/else:

5. keep returning 1 for n <= 2

6. elif n and its value (expression) is in dictionary, return that

7. else if it is not, set it as such
8. then return it (rather than the call of both functions)
'''

stored_ops = {}

def fibonacci(n):
    if n <= 2:
        return 1
    elif n in stored_ops:
        return stored_ops[n]
    else:
        stored_ops[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return stored_ops[n]

print(fibonacci(1) == 1)         # True
print(fibonacci(2) == 1)         # True
print(fibonacci(3) == 2)         # True
print(fibonacci(4) == 3)         # True
print(fibonacci(5) == 5)         # True
print(fibonacci(6) == 8)         # True
print(fibonacci(12) == 144)      # True
print(fibonacci(20) == 6765)     # True

# 10:

'''
rules:
1. find and return the *index* of the 1st Fib number specified by the arg
    so: arg 2 looks for 1st 2-digit Fib num, which is 13, and returns its index
    
2. however for some reason the 1st Fib num has index of 1, not 0

3. arg will be at least 2

4. have to set a new set_int_max_str_digits limit

input: int (digits)
output: int (index of 1st Fib num with that # of digits)

algo:
1. we'll reuse the procedural code
2. import sys, set up new 'set_int_max_str_digits' limit
3. keep initialization of first and second to 1, and result to 0

4. initialize 'counter' to 2, which will stand in for the index
    it's 2 because we start with 2 Fib numbers
    for the 1st operation, to get the 3rd Fib num, we increment counter by 1

5. make a while loop, while the length of the string of 'result' is less than input num
6. increment counter by 1 for each iteration
7. the rest is the same as in the procedural code

8. return counter (the index)
'''

import sys
sys.set_int_max_str_digits(50_000)

def find_fibonacci_index_by_length(num):
    first = 1
    second = 1
    
    result = 0
    counter = 2
    
    while len(str(result)) < num:
        counter += 1
        result = first + second
        first = second
        second = result
        
    return counter

# All of these examples should print True
# The first 12 fibonacci numbers are: 1 1 2 3 5 8 13 21 34 55 89 144
print(find_fibonacci_index_by_length(2) == 7)
print(find_fibonacci_index_by_length(3) == 12)
print(find_fibonacci_index_by_length(10) == 45)
print(find_fibonacci_index_by_length(16) == 74)
print(find_fibonacci_index_by_length(100) == 476)
print(find_fibonacci_index_by_length(1000) == 4782)

# Next example might take a little while on older systems
print(find_fibonacci_index_by_length(10000) == 47847)