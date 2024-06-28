print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")

cross_road = str(input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\" \n")).lower()

if cross_road == "left":
    lake = str(input("You come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across. \n")).lower()
    if lake == "wait":
        door_colour = str(input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n")).lower()
        if door_colour == "yellow":
            print("You win!")
        else:
            print("Wrong. Game over.")
    else: 
        print("The water was poison. Game over.")
else:
    print("Right is never right. Game over.")