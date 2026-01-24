def find_integers(elements):
    return [ element
            for element in elements
            if type(element) is int
    ]

    for element in elements:
        if isinstance(element, int):
            return element

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    