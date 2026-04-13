# 1-3:

class Dividing:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def divide(self):
        try:
            divided = self.num1 / self.num2
        except (ZeroDivisionError, ValueError) as e:
            print(e)
        else:
            print(divided)
        finally:
            print("End of the program.")

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
two_nums = Dividing(float(num1), float(num2))
two_nums.divide()

# 4-5:

class NegativeNumberError(Exception):
    pass
    # def __init__(self, message="Negative number entered; not allowed."):
    #     super().__init__(message)

num = float(input("Enter a number: "))
if num < 0:
    raise NegativeNumberError
print(f'Number is {num}.')

# 6:

def inverse_nums(lst):
    inverse_list = []
    
    for num in lst:
        try:
            inverse_list.append(1 / num)
        except TypeError:
            inverse_list.append(f"{num} is not divisible")
        except ZeroDivisionError:
            inverse_list.append(float('inf'))


        # if not isinstance(num, (int, float)):
        #     raise ValueError('Not every number is an integer or float.')
        # if num == 0 or num == 0.0:
        #     raise ZeroDivisionError('0 or 0.0 in the list.')

    return inverse_list

l1 = [5, 6, 7.5, 0, 'blah']
print(inverse_nums(l1))

# 8:

students = {'John': 25, 'Jane': 22, 'Doe': 30}

def get_age(name):
    try:
        return students[name]
    except KeyError:
        return "Student not found."
    
print(get_age('John'))
print(get_age('Johnny'))

# 9:

numbers = [1, 2, 3, 4, 5]

def lbyl_function_sixth_element(lst):
    if len(numbers) > 5:
        return numbers[5]
    return None
    
print(lbyl_function_sixth_element(numbers))

def afnp_function_sixth_element(lst):
    try:
        return numbers[5]
    except IndexError:
        return None
    
print(afnp_function_sixth_element(numbers))