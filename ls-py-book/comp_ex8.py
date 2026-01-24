my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

odd_keys = { key: len(key)
             for key in my_set
               if len(key) % 2 != 0 }
print(odd_keys)

# how to grab key from set
# how to key.string-ify

# Write a comprehension that creates a dict object whose keys 
# are strings and whose values are the length of the corresponding key. 
# Only keys with odd lengths should be in the dict. 
# Use the set given by my_set as the source of strings.