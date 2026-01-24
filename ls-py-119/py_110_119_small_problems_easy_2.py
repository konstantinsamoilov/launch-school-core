# 1, woof:

DEGREE = "\u00B0"

def dms(flt):
    degrees = str(flt)
    
    if '.' not in degrees:
        return f"{degrees}{DEGREE}00'00\""
    else:
        split_degrees = degrees.split(".") #
        degree_bits = "." + split_degrees[1]
        minutes = float(degree_bits) * 60
        
        split_time = str(minutes).split(".")
        seconds_string = "." + split_time[1]
        seconds = float(seconds_string) * 60
        
        return f"{split_degrees[0]}{DEGREE}{int(minutes):02}'{int(seconds):02}\""

# Further exploration:

DEGREE = "\u00B0"
CIRCLE = 360

def dms(flt):
    degrees = str(flt)
    
    if flt < -360: # LSBot helped figure this out
        degree_of_very_negative_float = flt
        while degree_of_very_negative_float < 0:
            degree_of_very_negative_float += 360
        return f"{degree_of_very_negative_float}{DEGREE}00'00\""
    
    if -360 < flt < 0:
        return f"{CIRCLE + flt}{DEGREE}00'00\""
    
    elif flt > 360:
        return f"{flt - CIRCLE}{DEGREE}00'00\""
    
    elif '.' not in degrees:
        return f"{degrees}{DEGREE}00'00\""
    
    else:
        split_degrees = degrees.split(".") #
        degree_bits = "." + split_degrees[1]
        minutes = float(degree_bits) * 60
        
        split_time = str(minutes).split(".")
        seconds_string = "." + split_time[1]
        seconds = float(seconds_string) * 60
        
        return f"{split_degrees[0]}{DEGREE}{int(minutes):02}'{int(seconds):02}\""

# 2:

def union(lst1, lst2):
    lst3 = lst1 + lst2
    union_set = set(lst3)
    return union_set

# 3 (what a hoot compared to the official solution):

def halvsies(lst):
    result_lst = [[], []]
    
    if len(lst) == 0:
        pass
    
    elif len(lst) == 1:
        result_lst[0] = lst
        
    elif len(lst) % 2 == 0:
        half_count = len(lst) // 2
        result_lst[0] = lst[:half_count]
        result_lst[1] = lst[half_count:]
    
    elif len(lst) % 2 != 0:
        half_count = len(lst) // 2 + 1
        result_lst[0] = lst[:half_count]
        result_lst[1] = lst[half_count:]
        
    return result_lst

# 4:

def find_dup(lst):
    seen = set()

    for num in lst:
        if num in seen:
            return num
        seen.add(num)
# Or:
def find_dup(lst):
    for num in lst:
        if lst.count(num) == 2:
            return num
        
# 5: 

def interleave(list1, list2):
    result = []
    zipped = zip(list1, list2)
    zipped_list = list(zipped)
    
    for pair in zipped_list:
        for el in pair:
            result.append(el)
    return result

# There are two more simple versions, one also using zip, aside from the official solution.

# 6:

def multiplicative_average(lst):
    result = 1
    
    for num in lst:
        result = result * num
        
    result = result / len(lst)
    
    return f"{result:.3f}"

# 7:

list1 = [3, 5, 7]
list2 = [9, 10, 11]

def multiply_list(l1, l2):
    result = []
    
    for el1, el2 in zip(l1, l2):
        result.append(el1 * el2)
    return result

# 8 (sigh, the official solution is a very simple comprehension... next time):

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def digit_list(num):
    str_num = str(num)
    
    result = []
          
    for el in str_num:
        result.append(DIGITS[el])
    return result

# 9 (using set to print):

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

def count_occurrences(lst):
    result = []
    for el in lst:
        result.append(f'{el} => {lst.count(el)}')
    
    set_result = set(result)
    
    for el in set_result:
        print(el)

count_occurrences(vehicles)

# Further exploration (LSBot helped):

vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck', 'suv']

def count_occurrences(lst):
    processed_words = []
    
    for el in lst:
        if el.lower() in processed_words:
            continue
        count = 0
        for item_to_check in lst: # "holding" on each element el and comparing it to every other in the list, other than those that get added to processed_words 
            if item_to_check.lower() == el.lower():
                count += 1
            
        print(f'{el} => {count}')
          
        processed_words.append(el.lower())

count_occurrences(vehicles)

# 10 (forgot about sum):

def average(lst):
    result = 0
    
    for num in lst:
        result += num
        
    result //= len(lst)
    
    return result