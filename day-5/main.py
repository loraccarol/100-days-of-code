import random

print("Welcome to the PyPassword Generator!")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input("How many symbols would you like?\n"))
n_numbers = int(input("How many numbers would you like?\n"))

password = []

for l in range(1, n_letters+1):
    teste = random.randrange(len(letters))
    password.append(letters[teste])

for s in range(1, n_symbols+1):
    teste = random.randrange(len(symbols))
    password.append(symbols[teste])

for n in range(1, n_numbers+1):
    teste = random.randrange(len(numbers))
    password.append(numbers[teste])

random.shuffle(password)

p_str = ""
for p in password:
    p_str += p

print(f"Here is your password: {p_str}")
