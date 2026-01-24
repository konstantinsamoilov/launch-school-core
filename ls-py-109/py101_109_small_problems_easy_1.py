# Easy 1
# 1

def abs_odd(num):
    if abs(num) % 2 != 0:
        return True
    else:
        return False

print(abs_odd(5))
print(abs_odd(6))

# Second pass:

def which_abs(num):
    return abs(num) % 2 != 0

print(which_abs(5))
print(which_abs(8))

# 2

def print_nums():
    for n in range(1, 100, 2):
        print(n)

print_nums()

# Second pass (+ further exploration):

start_odd = int(input("Enter the starting odd number: "))
end_odd = int(input("Enter the ending odd number: "))

for num in range(start_odd, end_odd + 1, 2):
    print(num)

# 3

for n in range(1, 100, 1):
    if n % 2 == 0:
        print(n)

# Second pass (+ further exploration):

for num in range(2, 100, 2):
    print(num)

# 4

SQM_TO_SQFT = 10.7639

room_length = float(input("Enter the length of your room, in meters. "))
room_width = float(input("Enter the width, in meters. "))

room_area = room_length * room_width

room_area_feet = room_area * SQM_TO_SQFT

print(f"The area of the room is {room_area:.2f} square meters.")
print(f"And {room_area_feet:.2f} square feet.")

# Second pass (+ further exploration):

# (Not the best code ever, but maybe one day...)
# 1 square meter == 10.7639 square feet
meters_or_feet = input("Do you want to measure in meters or feet? Type 'meters' or 'feet': ").casefold()

if meters_or_feet == 'meters':
    length_meters = float(input("Enter the length of the room in meters: "))
    width_meters = float(input("Enter the width of the room in meters: "))

    area_sq_meters = length_meters * width_meters
    area_sq_feet = area_sq_meters * 10.7639

    print(f'The area of the room is {area_sq_meters:.2f}.' 
          f' In feet, it is {area_sq_feet:.2f}.')
    
elif meters_or_feet == 'feet':
    length_feet = float(input("Enter the length of the room in feet: "))
    width_feet = float(input("Enter the width of the room in feet: "))
    
    area_sq_feet = length_feet * width_feet
    area_sq_meters = area_sq_feet / 10.7639

    print(f'The area of the room is {area_sq_feet:.2f}.' 
          f' In meters, it is {area_sq_meters:.2f}.')
    
# 5

bill_amount = float(input("What is the bill? "))
tip_percentage = float(input("What is the tip percentage? "))

tip_amount = (bill_amount / 100 * tip_percentage)
total_bill = bill_amount + tip_amount

print(f"Your tip amount is {tip_amount:.2f}.")
print(f"Your total bill amount is {total_bill:.2f}.")

# Second pass:

bill = float(input("What is the bill? "))
tip_percent = float(input("What is the tip %? "))

tip = (bill / 100) * tip_percent
total = bill + tip

print(f'The tip is ${tip:.2f}')
print(f'The total is ${total:.2f}')

# 6

while True:
    try:
        input_integer = int(input("Enter an integer greater than 0: "))
        if input_integer > 0:
            break
        print("No. Enter an integer greater than 0: ")
    except ValueError:
        print("Not a valid integer. Try again: ")

while True: 
    sum_or_product = input("Enter 's' to compute the sum, or 'p' to compute the product. ")
    if sum_or_product in ('s', 'p'):
        break
    print("Enter 's' or 'p'.")
    
if sum_or_product == 's':
    sum_total = 0
    for num in range(1, input_integer + 1):
        sum_total += num
    print(f"Sum of integers between 1 and {input_integer} is {sum_total}.")
    
elif sum_or_product == 'p':
    product_total = 1
    for num in range(1, input_integer + 1):
        product_total *= num
    print(f"Product of integers between 1 and {input_integer} is {product_total}.")
    
else: print("Oops. Unknown operation.")

# Second pass:

while True:
    try:
        num = int(input("Enter an integer greater than 0: "))
        if num > 0:
            break
        print("It needs to be greater than 0. ")
    except ValueError:
        print("Not a valid integer.")

operation = input("Enter 's' to compute the sum, or 'p' to compute the product: ").casefold()

if operation == 's':
    sum_num = 0
    for num in range(1, num + 1):
        sum_num += num
    print(f'The sum of the integers between 1 and {num} is {sum_num}.')

elif operation == 'p':
    prod_num = 1
    for num in range(1, num + 1):
        prod_num *= num
    print(f'The product of the integers between 1 and {num} is {prod_num}.')

# 7

def short_long_short(str1, str2):
    newstr = ''
    if len(str1) > len(str2):
        newstr = str2 + str1 + str2
        return newstr
    else:
        newstr = str1 + str2 + str1
        return newstr

# Second pass:

def short_long_short(str1, str2):
    if len(str1) > len(str2):
        new_str = str2 + str1 + str2
        return new_str
    else:
        new_str = str1 + str2 + str1
        return new_str

# 8

def is_leap_year(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

# Second pass:

def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
# 9

def is_leap_year(year):
    if year >= 1752:
        if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
            return True
        else:
            return False
    elif year < 1752:
        if year % 4 == 0:
            return True
        else:
            return False
        
# Second pass:

def is_leap_year(year):
    if year >= 1752:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False
    
    elif year < 1752:
        return year % 4 == 0
    
# 10

def multisum(num):
    numsum = 0
    for i in range(1, num + 1):
        if i % 3 == 0 or i % 5 == 0:
            numsum += i
    return numsum

# Second pass:

def multisum(num):
    summed = 0
    for n in range(1, num + 1):
        if n % 3 == 0 or n % 5 == 0:
            summed += n
    return summed

# 11

def utf16_value(el):
    utfsum = 0
    for char in el:
        utfsum += ord(char)
    return utfsum

# Second pass:

def utf16_value(string):
    ord_value = 0
    for char in string:
        ord_value += ord(char)
    return ord_value