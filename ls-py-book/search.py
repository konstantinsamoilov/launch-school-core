nums = [3, 1, 5, 9, 2, 6, 4, 7]
found_item = -1
index = 0

while index < len(nums):
    if nums[index] == 5:
        found_item = index
        break

    index += 1

print(found_item)

# Here -- why are we initializing found_item at -1 if we're going to reassign it to index anyway?