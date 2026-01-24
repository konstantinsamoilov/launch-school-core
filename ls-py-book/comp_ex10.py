import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break