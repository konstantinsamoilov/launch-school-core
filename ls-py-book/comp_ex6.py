my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

# result = []
# for number in my_list:
#     if number % 2 != 0:
#         result.append('odd')
#     else:
#         result.append('even')

# print(result)

def odd_or_even(number):
    return 'even' if number % 2 == 0 else 'odd'

result = [ odd_or_even(number)
          for number in my_list]
print(result)