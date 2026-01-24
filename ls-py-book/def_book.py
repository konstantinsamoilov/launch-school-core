def say(msg1, msg2, msg3='dummy message',
                    msg4='omitted message'):
    print(msg1)
    print(msg2)
    print(msg3)
    print(msg4)

say('a', 'b', 'c', 'd')
# a
# b
# c
# d

say('a', 'b', 'c')
# a
# b
# c
# omitted message

say('a', 'b')
# a
# b
# dummy message
# omitted message

# say('a', 'b', , 'd')
# a
# b
# d               # oops - expecting 'dummy message'
# omitted message # oops again - expected 'd'