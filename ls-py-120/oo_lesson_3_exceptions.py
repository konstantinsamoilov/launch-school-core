def foo1():

    # raise ZeroDivisionError('Got ZeroDivisionError')
    # raise ValueError('Got ValueError')
    # raise AttributeError('Got AttributeError')
    print('We should not be here')

def foo2():
    try:
        foo1()
    except ZeroDivisionError:
        print('Got ZeroDivisionError')

def foo3():
    try:
        foo2()
    except ValueError:
        print('Got ValueError')

foo3()

###

for value in ['abc', '0']:
    try:
        number = float(value)
        quotient = 3.0 / number
        break
    except ValueError as e:
        print("Oops! That's not a valid number.", e, '', sep='\n')
    except ZeroDivisionError as e:
        print('Oops! You tried to divide by zero!', e, '', sep='\n')
# Oops! That's not a valid number.
# could not convert string to float: 'abc'
#
# Oops! You tried to divide by zero!
# float division by zero

###

log_file = open("log_file.txt", "w")

try:
    open("no_such_file.txt", "r")
except OSError as e:
    print(f'{e.errno=}, {e.strerror=}, {e.filename=}', file=log_file)
    log_file.close()
    raise

###

for divisor in [2, 0]:
    try:
        result = 10 / divisor
    except ZeroDivisionError as e:
        print('Division by zero.')
    else:
        print(f'Result is {result}')

###

raise ValueError('This is a message!')

###

class ValidationError(Exception):
    def __init__(self, message="Invalid data"):
        super().__init__(message)

class ValidationError(Exception):
    def __init__(self):
        super().__init__("Invalid data")

###