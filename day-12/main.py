import random

print("Guessing Game")
print("I'm thinking of a number between 1 and 100.")

number_chosen = random.randint(1,100)

print(f"number chosen = {number_chosen}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number_tries = 0

if difficulty == "easy":
    number_tries = 10
if difficulty == "hard":
    number_tries = 5 

while number_tries > 0:
    print(f"You have {number_tries} attemps remaining to guess the number.")
    guess = int(input("Make a guess: "))

    if guess == number_chosen:
        print("You got it.")
        break
    elif guess < number_chosen:
        print("Too low.")
        number_tries -= 1
    elif guess > number_chosen:
        print("Too high.")
        number_tries -= 1
