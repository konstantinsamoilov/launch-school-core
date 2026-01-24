# 1:
# Loop:
munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

male_total = 0

for k, v in munsters.items():
    if v['gender'] == 'male':
        male_total += v['age']
        
print(male_total)

# Comprehension:
male_total_list = [v['age'] for v in munsters.values() if v['gender'] == 'male']
print(sum(male_total_list))

# 2:
# Loop:
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

sorted_lst = []

for l in lst:
    sorted_lst.append(sorted(l))
print(sorted_lst)

# Comprehension:
sorted_lst2 = [sorted(l) for l in lst]
print(sorted_lst2)

# 3:
# Loop:
lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

sorted_lst = []

for l in lst:
    sorted_lst.append(sorted(l, key=str))
print(sorted_lst)

# Comprehension:
sorted_lst2 = [sorted(l, key=str) for l in lst]
print(sorted_lst2)

# 4:
# Comprehension:
lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

new_dict = {sublist[0]: sublist[1] for sublist in lst}
print(new_dict)

# dict constructor also works:
new_dict2 = dict(lst)
print(new_dict2)

# 5:
lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def sum_of_odd_nums(sublist):
    odd_nums = [num for num in sublist if num % 2 != 0]
    return sum(odd_nums)

result = sorted(lst, key=sum_of_odd_nums)
print(result)

# 6:
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

new_lst = [{k: v + 1 for k, v in d.items()} for d in lst]
print(new_lst)

# 7:
# For loop:
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

lst_of_3 = []

for sublist in lst:
    lst_of_3_sublist = []
    for num in sublist:
        if num % 3 == 0:
            lst_of_3_sublist.append(num)        
    lst_of_3.append(lst_of_3_sublist)

print(lst_of_3)

# Comprehension:
lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

lst_of_3 = []

for sublist in lst:
    lst_of_3_sublist = [num for num in sublist if num % 3 == 0]
    lst_of_3.append(lst_of_3_sublist)

print(lst_of_3)

# 8:
dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}
lst = []

for value in dict1.values():
    if value['type'] == 'fruit':
        capitalized_colors = [color.capitalize() for color in value['colors']]
        lst.append(capitalized_colors)
    if value['type'] == 'vegetable':
        lst.append(value['size'].upper())
print(lst)

# 9: (all(all)) is funny but I find this easier to read than helper functions...
lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

result = []

for d in lst:
    if all(all(num % 2 == 0 for num in v) for v in d.values()):
        result.append(d)

print(result)

# 10:
import random

def make_uuid():
    uuid_chars = '0123456789abcdef'
    uuid_list = [random.choice(uuid_chars) for _ in range(0, 32)]
    uuid_string = ''.join(uuid_list)
    
    uuid_string = (uuid_string[0:8] + '-' 
    + uuid_string[8:12] + '-' 
    + uuid_string[12:16] + '-' 
    + uuid_string[16:20] + '-' 
    + uuid_string[20:])
    
    return uuid_string
    
make_uuid()

# 11:
# For loop:
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

vowels = 'aeiouAEIOU'
list_of_vowels = []

for lst in dict1.values():
    for s in lst:
        for char in s:
            if char in vowels:
                list_of_vowels.append(char)

print(list_of_vowels) # ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']

# Comprehension:
dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

vowels = 'aeiouAEIOU'
list_of_vowels = []

list_of_vowels += [char 
                   for lst in dict1.values()
                   for s in lst
                   for char in s
                   if char in vowels]
        
print(list_of_vowels)