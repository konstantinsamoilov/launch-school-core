print({1, 2, 3} in {1, 2, 3})          # False

# in with sets only checks whether a specific value is in the set.
# and in that line it's looking for a set of that, within that set

print('Butter' in cats)       # False 

# "string in list" must match a list element exactly.

print('Butter' in cats[3])    # True



my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

# Write some code that combines the sequences into a list of tuples. 
# Each tuple should contain one member of each sequence. 
# Print the final result so you can see all the values, which should look like this:

[('a', 'Alpha', None, 10),
 ('b', 'Bravo', True, 20),
 ('c', 'Charlie', False, 30)]

## a zip object isn't accessible by itself, i guess? if you call it, it displays a memory address.
## and you have to explicitly call "list" on it to display it. (or a tuple, etc)