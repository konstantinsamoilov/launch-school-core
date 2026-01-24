# Ask user for second number
# Ask user for operation
# Do operation
# Print result

LANGUAGE = 'en'

import json

# Open the JSON file for reading
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

print("=> choose language: 'en' or 'ru'")
LANGUAGE = input().lower()
if LANGUAGE not in MESSAGES:
    LANGUAGE = 'en'

def messages_func(key, lang='en'):
    return MESSAGES[lang][key]

def prompt(key):
    message = messages_func(key, LANGUAGE)
    print(f'=> {message}')

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

while True:

    prompt('welcome')

    # Ask user for first number
    prompt('first_number')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid_number')
        number1 = input()

    # Ask user for second number
    prompt('second_number')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid_number')
        number2 = input()

    prompt('operation_prompt')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('invalid_operation')
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) / float(number2)

    prompt('result')
    print(f"=> {output}")

    prompt('try_again')
    answer = input()

    if not answer or answer[0].lower() not in ['y', 'д']:
        break