destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']

def contains(element, lst):
    return element in lst

def contains(element, lst):
    for item in lst:
        if item == element:
            return True
    return False

def contains(element, lst):
    index = 0
    while index < len(lst):
        if lst[index] == element:
            return True
        index += 1
    return False

print(contains('Barcelona', destinations))  # True
print(contains('Nashville', destinations))  # False