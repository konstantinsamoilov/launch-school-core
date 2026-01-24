def is_empty(s):
    return s == ''
    # return len(s) == 0
    # return not s

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True