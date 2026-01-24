# def capitalize_words(string):
#     words = string.split(' ')
#     capitalized_words = []

#     for word in words:
#         capitalized_words.append(word.capitalize())

#     return ' '.join(capitalized_words)

# string = 'launch school tech & talk'
# result = capitalize_words(string)
# print(result)

def capitalize_words(string):
    return string.title()

string = 'launch school tech & talk'
result = capitalize_words(string)
print(result)