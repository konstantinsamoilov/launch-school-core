# 119 Practice Problems

# 4:
'''
Create a function that takes a list of integers as an argument and returns a tuple of two numbers that are closest together in value. If there are multiple pairs that are equally close, return the pair that occurs first in the list.

Rules:
1. Take a list of integers, return a tuple of 2 numbers that are closest in value
2. If multiple pairs are equally close, return the first one
3. (Implicit) The numbers don't have to be next to each other in the input list
4. (Implicit) If there are two numbers of the same value, that would be the smallest pair

Input: list
Output: tuple

Algo:
Init 'gap', set to -1
init 'return_tuple', set to ()

Outer for-loop, for index in range of length of input list:
    Inner for-loop, for inner index in range of index + 1 to length of input list:
        If the maximum of that pair - minimum of that pair is smaller than value that 'gap' refers to, or if gap is -1:
            Reassign gap to new gap with that expression result
            Reassign return_tuple to (int from outer loop, int from inner loop)

Return return_tuple
'''

def closest_numbers(lst):
    gap = -1
    return_tuple = ()

    for idx in range(len(lst)):
            for iidx in range(idx + 1, len(lst)):
                if max(lst[idx], lst[iidx]) - min(lst[idx], lst[iidx]) < gap or gap == -1:
                    gap = max(lst[idx], lst[iidx]) - min(lst[idx], lst[iidx])
                    return_tuple = (lst[idx], lst[iidx])

    print(gap)
    print(return_tuple)

    return return_tuple

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))

# 5:

'''
Create a function that takes a string argument and returns the character that occurs most often in the string. If there are multiple characters with the same greatest frequency, return the one that appears first in the string. When counting characters, consider uppercase and lowercase versions to be the same.

Rules:
1. Return the char that occurs most often in input string
2. If multiple chars have same greatest frequency, return the first one
3. Uppercase + lowercase versions count as one
Implicit:
1. Spaces / other characters could be returned

Input: string
Output: string (char)
Also: dictionary

Algorithm:
Reassign input string to lowercased version of input string
Create 'chars_and_counts' empty dictionary

For-loop over elements in lowercased input string:
    To dictionary, add element as key and element's count in input string as value
    (Dictionary order is preserved, so we can trust it.)

For-loop over char and count in dictionary items:
    If count is equal to the max of the list of dictionary values:
        Return the associated char
'''

def most_common_char(input_str):
    input_str = input_str.lower()

    chars_and_counts = {}

    for el in input_str:
        chars_and_counts[el] = input_str.count(el)

    for char, count in chars_and_counts.items():
        if count == max(list(chars_and_counts.values())):
            return char

print(most_common_char('Hello World') == 'l')
print(most_common_char('Mississippi') == 'i')
print(most_common_char('Happy birthday!') == 'h')
print(most_common_char('aaaaaAAAA') == 'a')

my_str = 'Peter Piper picked a peck of pickled peppers.'
print(most_common_char(my_str) == 'p')

my_str = 'Peter Piper repicked a peck of repickled peppers. He did!'
print(most_common_char(my_str) == 'e')

# 6:

'''
Create a function that takes a string argument and returns a dict object in which the keys represent the lowercase letters in the string, and the values represent how often the corresponding letter occurs in the string.

Rules:
1. Return a dict object in which the keys are lowercase letters in input string,
2. And values are counts of those letters in the string.

Input: string
Output: dict

Algorithm:
Init a 'result_dict' empty dict

For-loop over char in input string:
    If char is lowercase and alphabetic:
        Add char as key in result_dict and its count in input string as value

Return result_dict
'''
def count_letters(s):
    result_dict = {}

    for char in s:
        if char.isalpha() and char.islower():
            result_dict[char] = s.count(char)

    return result_dict

expected = {'w': 1, 'o': 2, 'e': 3, 'b': 1, 'g': 1, 'n': 1}
print(count_letters('woebegone') == expected)

expected = {'l': 1, 'o': 1, 'w': 1, 'e': 4, 'r': 2,
            'c': 2, 'a': 2, 's': 2, 'u': 1, 'p': 2}
print(count_letters('lowercase/uppercase') == expected)

expected = {'u': 1, 'o': 1, 'i': 1, 's': 1}
print(count_letters('W. E. B. Du Bois') == expected)

print(count_letters('x') == {'x': 1})
print(count_letters('') == {})
print(count_letters('!!!') == {})

# 7:

'''
Create a function that takes a list of integers as an argument and returns the number of identical pairs of integers in that list. For instance, the number of identical pairs in [1, 2, 3, 2, 1] is 2: occurrences each of both 2 and 1.

If the list is empty or contains exactly one value, return 0.

If a certain number occurs more than twice, count each complete pair once. For instance, for [1, 1, 1, 1] and [2, 2, 2, 2, 2], the function should return 2. The first list contains two complete pairs while the second has an extra 2 that isn't part of the other two pairs.

Rules:
1. Return the number of pairs of integers in input list.
2. Return 0 if list empty or one value.
3. Count each pair, no matter if it's the same kind of pair.

Input: list of integers
Output: integer (count of pairs)
Also: dictionary

Algorithm:
Guard for lst of 0 or 1: return 0

Init a result_count, point to 0
Init a 'num_in_list' dictionary

For-loop over each integer in input list:
    If it's in the list (via being in the dictionary) and currently unpaired ('half')
        Increment result_count by 1
        Set its dictionary value to 'none'
    Else:
        Set it as a key in the dictionary and set 'half' as value

Return result_count
'''

def pairs(lst):
    if len(lst) < 2:
        return 0

    result_count = 0
    num_in_list = {}
    
    for num in lst:
        if num in num_in_list and num_in_list[num] == 'half':
            result_count += 1
            num_in_list[num] = 'none'
        else:
            num_in_list[num] = 'half'

    return result_count

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

# 8:

'''
Create a function that takes a non-empty string as an argument. The string consists entirely of lowercase alphabetic characters. The function should return the length of the longest vowel substring. The vowels of interest are "a", "e", "i", "o", and "u".

Rules:
1. Return length of longest vowel substring

Input: string (lowercase, alphabetic)
Output: integer
Also: ...

Algorithm:
Init a running_count, point to 0
Init a list_of_counts, point to []
Init a 'vowels' string

For-loop over letter in input string:
    If letter is in vowels:
        Increment running_count by 1
    Else:
        Append running_count to list_of_counts
        Reassign running_count to 0

After the loop, append the final current running_count to list_of_counts

Return maximal integer in list_of_counts
'''

def longest_vowel_substring(s):
    running_count = 0
    list_of_counts = []
    vowels = 'aeiou'

    for letter in s:
        if letter in vowels:
            running_count += 1
        else:
            list_of_counts.append(running_count)
            running_count = 0

    list_of_counts.append(running_count)

    return max(list_of_counts)

print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)

# 9:

'''
Create a function that takes two string arguments and returns the number of times that the second string occurs in the first string. Note that overlapping strings don't count: 'babab' contains 1 instance of 'bab', not 2.

You may assume that the second argument is never an empty string.

Rules:
1. Return count of second input string occurring in first input string.
2. Overlapping strings don't count.
3. Second input string is never empty.

Input: Two strings
Output: Integer (count)
Also: 

Algorithm:
Maybe we can split first string by second string
    The count will be how many elements there are in the list (split_list) resulting from split, or that number minus one

Return length of split_list minus one
'''

def count_substrings(str1, str2):
    split_list = str1.split(str2)

    return len(split_list) - 1

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

# 10:

'''
Create a function that takes a string of digits as an argument and returns the number of even-numbered substrings that can be formed. For example, in the case of '1432', the even-numbered substrings are '14', '1432', '4', '432', '32', and '2', for a total of 6 substrings.

If a substring occurs more than once, you should count each occurrence as a separate substring.

Rules:
1. Return the count of even-numbered substrings in input string
2. Same substrings are all counted

Input: string
Output: integer (count)
Also: list

Algorithm:
Need every single substring, so maybe nested loops

Init 'list_of_substrings', point to empty list
Init 'even_substrings_count', point to 0

We'll add all substrings to a list with a nested for-loop.

For start_idx in range of length of input string:
    For end_idx in range of start_idx to length of input string:
        Append string[start_idx:end_idx + 1] to list_of_substrings

Another for-loop to check for evenness:
For substring in list_of_substrings:
    If the integer representation of the substring is even:
        Increment even_substrings_count by 1

Return even_substrings_count
'''

def even_substrings(s):
    list_of_substrings = []
    even_substrings_count = 0

    for start_idx in range(len(s)):
        for end_idx in range(start_idx, len(s)):
            list_of_substrings.append(s[start_idx:end_idx + 1])

    print(list_of_substrings)

    for substring in list_of_substrings:
        if int(substring) % 2 == 0:
            even_substrings_count += 1

    return even_substrings_count

print(even_substrings('1432') == 6)
print(even_substrings('3145926') == 16)
print(even_substrings('2718281') == 16)
print(even_substrings('13579') == 0)
print(even_substrings('143232') == 12)

# 11:

'''
Create a function that takes a nonempty string as an argument and returns a tuple consisting of a string and an integer. If we call the string argument s, the string component of the returned tuple t, and the integer component of the tuple k, then s, t, and k must be related to each other such that s == t * k. The values of t and k should be the shortest possible substring and the largest possible repeat count that satisfies this equation.

You may assume that the string argument consists entirely of lowercase alphabetic letters.

Rules:
1. Take nonempty lowercase alphabetic string. 
2. Return a tuple of the shortest possible substring and the largest possible repeat count that equals input string.

Input: string
Output: tuple (string, integer)
Also: 

Algorithm:
Looking for repetition.

Might select only the substrings starting from the beginning, because one of those, multiplied, will equal input string.

Init 'starting_substrings', point to empty list

For-loop over index in range of length of input string:
    Append to starting_substrings a slice of input string from start to index + 1

Now we have our list, and can look for the first substring, thus multiplied by the largest amount, that equals input string.
We'll need a nested loop.

For-loop over substring in starting_substrings:
    Inner for-loop over 'multiplier' in range of length of string + 1:
        If substring * multiplier is equal to s:
            Return the tuple (substring, multiplier)

Because of the ask of the problem, we are able to iterate over all possible multipliers of substrings starting at the shortest, and get a correct result more straightforwardly than it seems at first.
'''

def repeated_substring(s):
    starting_substrings = []

    for idx in range(len(s)):
        starting_substrings.append(s[:idx + 1])

    print(starting_substrings)

    for substring in starting_substrings:
        for mult in range(len(s) + 1):
            if substring * mult == s:
                return (substring, mult)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))

# 12:

'''
Create a function that takes a string as an argument and returns True if the string is a pangram, False if it is not.

Pangrams are sentences that contain every letter of the alphabet at least once. For example, the sentence "Five quacking zephyrs jolt my wax bed." is a pangram since it uses every letter at least once. Note that case is irrelevant.

Rules:
1. Return True if input string is pangram, False if not.
2. Pangram: has every letter of alphabet.
3. Case is irrelevant.

Input: string
Output: boolean
Also: set

Algorithm:
Init 'alphabet' string
Init 'in_string' set

For-loop over char in string:
    If LOWERCASED char is alphabetic:
        Add char to 'in_string'

Compare length of 'alphabet' to 'in_string'. 
If equal, return True. If not, False
'''

def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    in_string = set()

    for char in s:
        if char.isalpha() and char.lower() in alphabet:
            in_string.add(char.lower())

    print(in_string)

    if len(alphabet) == len(in_string):
        return True
    return False

print(is_pangram('The quick, brown fox jumps over the lazy dog!') == True)
print(is_pangram('The slow, brown fox jumps over the lazy dog!') == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in fog.") == True)
print(is_pangram("A wizard’s task is to vex chumps quickly in fog.") == False)
print(is_pangram("A wizard’s job is to vex chumps quickly in golf.") == True)

my_str = 'Sixty zippers were quickly picked from the woven jute bag.'
print(is_pangram(my_str) == True)

# 13:

'''
Create a function that takes two strings as arguments and returns True if some portion of the characters in the first string can be rearranged to match the characters in the second. Otherwise, the function should return False.

You may assume that both string arguments only contain lowercase alphabetic characters. Neither string will be empty.

Rules: 
1. Return True if portion of chars in 1st string can be rearranged to match 2nd string. False if not.
2. Input strings are fully lowercase and alphabetic. Neither is empty.

Input: two strings
Output: boolean

Algorithm:
I thought a dictionary would be needed, but no. Just one for-loop:

For char in str2:
    if char is in str1 and the count of that char in str1 is more or equal to the count of that char in str2:
        continue checking
    else:
        return False immediately

After all checks, if every character passes, return True
~~~

for char in str2:
    if char in str1 

'''
def unscramble(str1, str2):
    for char in str2:
        if char in str1 and str1.count(char) >= str2.count(char):
            continue
        else:
            return False

    return True

print(unscramble('ansucchlohlo', 'launchschool') == True)
print(unscramble('phyarunstole', 'pythonrules') == True)
print(unscramble('phyarunstola', 'pythonrules') == False)
print(unscramble('boldface', 'coal') == True)
print(unscramble('olc', 'cool') == False)

# 14:

'''
Create a function that takes a single integer argument and returns the sum of all the multiples of 7 or 11 that are less than the argument. If a number is a multiple of both 7 and 11, count it just once.

For example, the multiples of 7 and 11 that are below 25 are 7, 11, 14, 21, and 22. The sum of these multiples is 75.

If the argument is negative, return 0.

Rules:
1. Return SUM of all multiples of 7 or 11 that are less than the argument.
2. If a number is a multiple of both 7 and 11, count it only once (so add it to a collection once)
3. If input is negative, return 0.

Input: integer
Output: integer (sum)
Also: range, set

Algorithm:
Guard for 0 or lesser argument:
    Return 0

set_of_multiples = set()

For-loop for each_num in range(1, num + 1):
    if each_num is a multiple of 7 or multiple of 11,
        add it to set

return sum of set_of_multiples
'''

def seven_eleven(num):
    if num <= 0:
        return 0

    set_of_multiples = set()

    for each_num in range(1, num):
        if each_num % 7 == 0 or each_num % 11 == 0:
            set_of_multiples.add(each_num)

    return sum(set_of_multiples)

print(seven_eleven(10) == 7)
print(seven_eleven(11) == 7)
print(seven_eleven(12) == 18)
print(seven_eleven(25) == 75)
print(seven_eleven(100) == 1153)
print(seven_eleven(0) == 0)
print(seven_eleven(-100) == 0)

# 15:

'''
Create a function that takes a string argument that consists entirely of numeric digits and computes the greatest product of four consecutive digits in the string. The argument will always have more than 4 digits.

Rules:
1. Compute greatest product of 4 consecutive digits in input string.
2. Input will always have 5+ digits.

Input: string
Output: integer (product)
Also: list

Algorithm:
init list_of_substrings, point it to []

for-loop over the start index in range of length of string
    for-loop over the end index in range of start index to length of string
        append to list each slice from string

init products, point it to []

for substring in list_of_substrings,
    if the substring is 4 chars, 
        init 'product', point it to 1
            for char in substring,
                update product with new multiplication of each integer representation of char
            append to products product

return maximal product in products
'''
def greatest_product(s):
    list_of_substrings = []

    for start_idx in range(len(s)):
        for end_idx in range(start_idx, len(s)):
            list_of_substrings.append(s[start_idx:end_idx + 1])

    products = []

    for substring in list_of_substrings:
        if len(substring) == 4:
            product = 1
            for char in substring:
                product *= int(char)
            products.append(product)

    return max(products)

print(greatest_product('23456') == 360)      # 3 * 4 * 5 * 6
print(greatest_product('3145926') == 540)    # 5 * 9 * 2 * 6
print(greatest_product('1828172') == 128)    # 1 * 8 * 2 * 8
print(greatest_product('123987654') == 3024) # 9 * 8 * 7 * 6

# 16:

'''
Create a function that returns the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. You may assume that the input string contains only alphanumeric characters.

Rules:
1. Return count of distinct case-insensitive alphanumeric chars that occur 2+ in input string
2. Input string only has alphanumeric chars.

Input: string
Output: integer (count)
Also: set

Algorithm:
Init 'multiple_chars', point to empty set

Reassign string to lowercased version

For-loop over char in string:
    If the count of char in string is > 1,
        Append to set the char

Return the length of 'multiple_chars'
'''

def distinct_multiples(s):
    multiple_chars = set()
    s = s.lower()

    for char in s:
        if s.count(char) > 1:
            multiple_chars.add(char)

    return len(multiple_chars)

print(distinct_multiples('xyz') == 0)               # (none)
print(distinct_multiples('xxyypzzr') == 3)          # x, y, z
print(distinct_multiples('xXyYpzZr') == 3)          # x, y, z
print(distinct_multiples('unununium') == 2)         # u, n
print(distinct_multiples('multiplicity') == 3)      # l, t, i
print(distinct_multiples('7657') == 1)              # 7
print(distinct_multiples('3141592653589793') == 4)  # 3, 1, 5, 9
print(distinct_multiples('2718281828459045') == 5)  # 2, 1, 8, 4, 5

# 17:
'''
Create a function that takes a list of integers as an argument. The function should determine the minimum integer value that can be appended to the list so the sum of all the elements equals the closest prime number that is greater than the current sum of the numbers. For example, the numbers in [1, 2, 3] sum to 6. The nearest prime number greater than 6 is 7. Thus, we can add 1 to the list to sum to 7.

Notes:
The list will always contain at least 2 integers.
All values in the list must be positive (> 0).
There may be multiple occurrences of the various numbers in the list.

Rules:
1. Determine minimum integer that can be added to list so the sum equals closest prime number that's > CURRENT sum
2. List will have 2+ integers
3. All ints in list are positive
4. Ints in list can repeat

Input: list (of integers)
Output: integer (to be added to list)
Also: range

Algorithm:

As the counter counts up, if you divide summed + counter and it doesn't equal 1 for anything except
for dividing by 1 and itself, then we set that as 'nearest_prime'

Init 'nearest_prime', point to 0

Init 'summed', point to sum of input list

Init 'counter', point to 1

Init 'summed_and_counter', point to summed + counter

while-loop of 'nearest_prime' == 0:
    for-loop over 'dividing_by' in range of summed_and_counter + 1:
        if sum + counter 

We have nearest_prime
'''
def nearest_prime_sum(lst):
    nearest_prime = 0
    summed = sum(lst)
    counter = 1
    summed_and_counter = summed + counter
    # 7 % 7 range(2, curr)
    # 7 2...6 don't have modulo 0 prime  

# (nearest_prime_sum([5, 2]) == 4)
#     sum = 7
#     when we do [potential prime number] % [an iterating dividing_by] (2, 3, 4, 5, 6): if all of them are 0, then it's not a prime number
# 8 [2, 4] not prime 
# [2, 3, 4, 5, 6, 7]
# 8 % num == 0
# 8 is divisible by any of the nums among [2, 3, 4, 5, 6, 7]
# 2 num - 1 
'''
a whole number greater than 1 that cannot be exactly divided by any whole number other than itself and 1 (e.g. 2, 3, 5, 7, 11).
'''
# so if you were to iterate potential prime number dividing by 2, 3, 4, 5, 6 and put the results into a LIST, if any of them are not 1, it's a prime number
    
    while nearest_prime == 0:
        
    


        for dividing_by in range(1, summed_and_counter + 1):
            if summed_and_counter == 1 only when it's divided by 1 and summed_and_counter
            
            if summed_and_counter != 1 when divided by anything between 2 and summed_and_counter - 1



            / dividing_by == 
            # if you divide summed + counter and it doesn't equal 1 for anything except
# for dividing by 1 and itself, then we set that as 'nearest_prime'
            counter += 1
                
# range(summed_and_counter + 1)
# range(0, summed_and_counter + 1)
# 0.... summed_and_counter 

print(nearest_prime_sum([1, 2, 3]) == 1)        # Nearest prime to 6 is 7
print(nearest_prime_sum([5, 2]) == 4)           # Nearest prime to 7 is 11
print(nearest_prime_sum([1, 1, 1]) == 2)        # Nearest prime to 3 is 5
print(nearest_prime_sum([2, 12, 8, 4, 6]) == 5) # Nearest prime to 32 is 37

# Nearest prime to 163 is 167
print(nearest_prime_sum([50, 39, 49, 6, 17, 2]) == 4)

#  summed_and_counter + 1 % dividing_by == 0:

# 18:

'''
Create a function that takes a list of integers as an argument. Determine and return the index N for which all numbers with an index less than N sum to the same value as the numbers with an index greater than N. If there is no index that would make this happen, return -1.

If you are given a list with multiple answers, return the index with the smallest value.

The sum of the numbers to the left of index 0 is 0. Likewise, the sum of the numbers to the right of the last element is 0.

Rules:
1. Return index N where nums with index less than N are == to nums with index greater than N.
    1.5. So this DOES NOT include the number with index N
2. Return -1 if it doesn't happen.
3. If there are multiple answers, return smallest index.
4. Sum of nums to left of index 0 is 0. Likewise for sum of numbers to right of last element.

Input: list
Output: index
Also: 

Algorithm: 
Iteratively compare slices of left to right of N
    If any of them are equal
        return N
    Else
        return -1

[1, -1, 2] 0, 1, 2 0 ~ len(list) - 1

For index in range(0, len(list) + 1),
    if the slice of input list[0:N + 1] == slice[N:],
        return N

'''
# [100, 5, -5]
def equal_sum_index(lst):
    for idx in range(len(lst)): # 0, 1
        if sum(lst[0:idx]) == sum(lst[idx + 1:]):
            # print(idx)
            return idx
        # else:
        #     print(f'we return -1 at idx {idx}')
        #     return -1
    return -1 

'''
1. answer: 0
[100, 5, -5]
left sum = lst[0:idx] = 0
right sum = lst[idx+1:] = 0
return curr idx 0 

2. answer: last element
[5, -5, 100] , curr idx = 2
left sum = 5 - 5 = 0 = lst[0:idx]
right sum = 0 = lst[idx+1:] = lst[3:]
'''

print(equal_sum_index([1, 2, 4, 4, 2, 3, 2]) == 3)
print(equal_sum_index([7, 99, 51, -48, 0, 4]) == 1)
print(equal_sum_index([17, 20, 5, -60, 10, 25]) == 0)
print(equal_sum_index([0, 2, 4, 4, 2, 3, 2]) == -1)

# The following test case could return 0 or 3. Since we're
# supposed to return the smallest correct index, the correct
# return value is 0.
print(equal_sum_index([0, 20, 10, -60, 5, 25]) == 0)