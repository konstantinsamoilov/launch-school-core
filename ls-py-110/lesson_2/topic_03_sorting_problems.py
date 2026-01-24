# # 1:
# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# print(sorted(lst))
# print(sorted(lst, reverse=True))

# # 2:
# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# lst.sort()
# print(lst)

# lst.sort(reverse=True)
# print(lst)

# # 3:
# lst = [10, 9, -6, 11, 7, -16, 50, 8]

# lst.sort(key=str)
# print(lst)

# lst.sort(key=str, reverse=True)
# print(lst)

# 4:
books = [
    {
        'title': 'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'published': '1967',
    },
    {
        'title': 'The Book of Kells',
        'author': 'Multiple Authors',
        'published': '800',
    },
    {
        'title': 'War and Peace',
        'author': 'Leo Tolstoy',
        'published': '1869',
    },
]

def func(lst):
    return int(lst['published'])

books.sort(key=func)
print(books)