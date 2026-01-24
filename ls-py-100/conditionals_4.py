weather = 'sunny'

# if weather == 'sunny':
#     print(f"It's a beautiful day!")
# elif weather == 'rainy':
#     print(f"It's also a beautiful day!")
# else:
#     print(f"whatever...")

match weather:
    case 'sunny':
        print(f"It's a beautiful day!")
    case 'rainy':
        print(f"It's a beautiful rainy day!")
    case 'snowy':
        print(f"IT'S SNOWING!!!")