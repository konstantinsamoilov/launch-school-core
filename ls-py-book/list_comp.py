""" squares = [ number * number for number in range(5) ]
print(squares)
 """



""" squares = []
for number in range(5):
    square = number * number
    squares.append(square)

print(squares) """



""" multiples_of_6 = [ number for number in range(20)
                    if number % 6 == 0 ]
print(multiples_of_6) """



""" even_squares = [ number * number
                  for number in range(10)
                  if number % 2 == 0 ]
print(even_squares) """



cats_colors = {
    'Tess':   'brown',
    'Leo':    'orange',
    'Fluffy': 'gray',
    'Ben':    'black',
    'Kat':    'orange',
}

""" upper_pairs = [ (name.upper(), color.upper()) for name, color in cats_colors.items() ]
print(upper_pairs) """

names = [ name.upper()
       for name in cats_colors
       if cats_colors[name] == 'orange' 
       if name[0] == 'L' ]
print(names)