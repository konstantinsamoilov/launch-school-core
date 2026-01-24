# 1:
produce = {
    'apple': 'Fruit',
    'carrot': 'Vegetable',
    'pear': 'Fruit',
    'broccoli': 'Vegetable',
}

def select_fruit(dct):
    fruit_dict = {}
    for k, v in dct.items():
        if v == 'Fruit':
            fruit_dict[k] = v
    return fruit_dict

print(select_fruit(produce)) # { apple: 'Fruit', pear: 'Fruit' }

# 2:

def double_numbers(numbers):
    stored_pops = []

    while numbers:
        stored_pops.append(numbers.pop()) 
    stored_pops.reverse()

    pop_idx = 0

    while len(numbers) != len(stored_pops):
        numbers.append(stored_pops[pop_idx] * 2)
        pop_idx += 1

    return numbers

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_numbers(my_numbers)) # [2, 8, 6, 14, 4, 12]
print(my_numbers)                 # [2, 8, 6, 14, 4, 12]

# Forgot about range(len(var))...
def double_numbers(numbers):
    for idx in range(len(numbers)):
        numbers[idx] *= 2
    return numbers

# 3:

def double_odd_idx_nums(numbers):
    idx_counter = 0
    result = []

    while idx_counter < len(numbers):
        if idx_counter % 2 != 0:
            result.append(numbers[idx_counter] * 2)
        idx_counter += 1

    return result

my_numbers = [1, 4, 3, 7, 2, 6]
print(double_odd_idx_nums(my_numbers)) # [2, 4, 6, 14, 2, 6]
print(my_numbers) # [1, 4, 3, 7, 2, 6]

# 4:

def multiply(numbers, multiplier):
    result = []

    for n in numbers:
        result.append(n * multiplier)

    return result

my_numbers = [1, 4, 3, 7, 2, 6]
print(multiply(my_numbers, 3))  # [3, 12, 9, 21, 6, 18]