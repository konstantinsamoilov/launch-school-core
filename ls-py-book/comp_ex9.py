def factorial(num):
    result = 1
    while num > 0:
        result *= num
        num -= 1
    return result

def factorial(num):
    result = 1
    for number in range(num, 0, -1):
        result *= number

    return result

# def factorial(num):
#     result = 1
#     counter = 1
#     while counter <= num:
#         result *= counter
#         counter += 1
#     return result

print(factorial(4))
print(factorial(5))