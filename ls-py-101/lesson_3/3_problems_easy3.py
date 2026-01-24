# Question 1

numbers = [1, 2, 3, 4]

numbers.remove(1)
numbers.remove(2)
numbers.remove(3)
numbers.remove(4)

while numbers:
    numbers.pop()

numbers = []

print(numbers)

# Question 5

def is_color_valid(color):
    return color == "blue" or color == "green"
        
def is_color_valid(color):
    return color in ["blue", "green"]