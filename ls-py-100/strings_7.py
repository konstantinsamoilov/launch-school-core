def is_empty_or_blank(s):
    return s.strip(' ') == ''
    # return len(s.strip(' ')) == 0
    # return not s.strip(' ')

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True