number1 = input('Enter the first number: ')
number2 = input('Enter the second number: ')
mult = float(number1) * float(number2)

print(f'{number1} * {number2} = {mult}')


def multiply(left, right):
    return left * right

def get_number(prompt):
    entry = input(prompt)
    return float(entry)

first_number = get_number('Enter the first number: ')
second_number = get_number('Enter the second number: ')
product = multiply(first_number, second_number)

print(f'{first_number} * {second_number} = {product}')