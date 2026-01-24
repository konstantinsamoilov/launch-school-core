# # Question 2

# str1 = "Come over here!"  # True
# str2 = "What's up, Doc?"  # False

# def exclamation_or_not(str):
#     if str[-1] == '!':
#         print(True)
#     else:
#         print(False)

# exclamation_or_not(str1)
# exclamation_or_not(str2)

# # print(str1.endswith("!"))
# # print(str2.endswith("!"))

# # Question 3

# famous_words = "seven years ago..."

# full_famous_words = f"Four score and {famous_words}"
# full_famous_words2 = "Four score and " + famous_words

# # Question 4

# munsters_description = "the Munsters are CREEPY and Spooky."
# print(munsters_description.capitalize())

# # Question 5

# munsters_description = "The Munsters are creepy and spooky."
# print(munsters_description.swapcase())

# # Question 6

# str1 = "Few things in life are as important as house training your pet dinosaur."
# str2 = "Fred and Wilma have a pet dinosaur named Dino."

# print("Dino" in str1)
# print("Dino" in str2)

# # Questions 7 & 8

# flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]

# flintstones.append("Dino")

# flintstones.extend(["Dino", "Hoppy"])

# print(flintstones)

# # Question 9

# advice = "Few things in life are as important as house training your pet dinosaur."

# print(advice.split("house")[0])

# # Question 10

advice = "Few things in life are as important as house training your pet dinosaur."

print(advice.replace("important", "urgent"))