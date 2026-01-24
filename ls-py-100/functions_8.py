def greet(isocode):
    match isocode:
        case 'en':
            return 'Hi!'
        case 'ru':
            return 'privyet!!!'
        case 'de':
            return 'halloooo'

print(greet('en'))
print(greet('ru'))
print(greet('de'))