max = '0'
for number in ['10', '2', '34', '6', '25']:
#   print('max =', max, 'number =', number,
#          'number > max =', number > max)
    if int(number) > int(max):
        max = number

print('max value is', max)