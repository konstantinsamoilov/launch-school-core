scores = [96, 47, 113, 89, 100, 102]

# count = 0

# for score in scores:
#     if score >= 100:
#         count += 1

hundos = [score for score in scores if score >= 100]

print(len(hundos))