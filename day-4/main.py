import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def print_img(choice):
    imgs = [rock, paper, scissors]
    print(imgs[choice])

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

pc_choice = random.randint(0, 2)

if choice >= 3 or choice < 0:
    print("Invalid number.")
else:
    print_img(choice=choice)
    print("Computer chose:")
    print_img(choice=pc_choice)
    if choice == pc_choice:
        print("It's a draw")
    elif (choice == 0 and pc_choice == 2) or (choice == 1 and pc_choice == 0) or (choice == 2 and pc_choice == 1):
        print("You win!")
    elif (choice == 0 and pc_choice == 1) or (choice == 1 and pc_choice == 2) or (choice == 2 and pc_choice == 0):
        print("You lose!")
    else:
        print("You lose!")