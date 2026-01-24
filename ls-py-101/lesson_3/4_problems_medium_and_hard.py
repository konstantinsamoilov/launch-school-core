# # Question 1

# counter = 1

# while counter < 11: # for padding in range(1, 11):
#     print('-' * counter + 'The Flintstones Rock!') # print(f'{"-" * padding}The Flintstones Rock!')
#     counter += 1

# # Question 2

# def factors(number):
#     divisor = number
#     result = []
#     while divisor > 0:
#         if number % divisor == 0:
#             result.append(number // divisor)
#         divisor -= 1
#     return result

# # Question 4

# import math
# print(math.isclose(0.3 + 0.6, 0.9))

# Question 5

# import math
# nan_value = float("nan")
# print(math.isnan(nan_value))
# # doesn't work: print(nan_value == float("nan"))

# Hard - Question 4

def is_dot_separated_ip_address(input_string):
    dot_separated_words = input_string.split(".")

    if len(dot_separated_words) != 4:
        return False

    while len(dot_separated_words) > 0:
        word = dot_separated_words.pop()
        if not is_an_ip_number(word):
            return False

    return True

def is_an_ip_number(str):
    if str.isdigit():
        number = int(str)
        return 0 <= number <= 255
    return False