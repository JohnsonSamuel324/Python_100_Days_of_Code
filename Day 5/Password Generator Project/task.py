letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))

# EASY
import random
easy_pass = ""
for letter in range(0, nr_letters):
    easy_pass += letters[random.randint(0, len(letters) - 1)]
for number in range(0, nr_numbers):
    easy_pass += numbers[random.randint(0, len(numbers) - 1)]
for symbol in range(0, nr_symbols):
    easy_pass += symbols[random.randint(0, len(symbols) - 1)]
print("EASY:")
print("Password: " + easy_pass)

# HARD
hard_pass_chars = []
hard_pass = ""
# Grab the random letters, numbers and symbols
for letter in range(0, nr_letters):
    hard_pass_chars.append(letters[random.randint(0, len(letters) - 1)])
for number in range(0, nr_numbers):
    hard_pass_chars.append(numbers[random.randint(0, len(numbers) - 1)])
for symbol in range(0, nr_symbols):
    hard_pass_chars.append(symbols[random.randint(0, len(symbols) - 1)])

print(hard_pass)
# Randomize order of characters
for characters in range(0, len(hard_pass_chars)):
    randint = random.randint(0, len(hard_pass_chars) - 1)
    hard_pass += hard_pass_chars[randint]
    hard_pass_chars.pop(randint)

print("HARD:")
print("Password: " + hard_pass)