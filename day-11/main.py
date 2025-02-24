import random
from os import system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def blackjack():

    play = input("Do you want to play Blackjack? Type 'y' or 'n': ")

    continue_play = True

    if play == 'y':
        players_cards = random.sample(cards, 2)
        comp_cards = random.sample(cards, 1)

        while continue_play:

            print(f"Your cards: {players_cards}, score: {sum(players_cards)}")
            print(f"Computer's first card: {comp_cards}, score: {sum(comp_cards)}")

            another_card = input("Type 'y' to get another card, type 'n' to pass: ")

            if another_card == 'y':
                players_cards.append(random.choice(cards))
                if sum(players_cards) >= 21 or sum(comp_cards) >= 21:
                    continue_play = False
            else:
                if sum(comp_cards) < 17:
                    comp_cards.append(random.choice(cards))
                continue_play = False
            
        print(f"Your final cards: {players_cards}, score: {sum(players_cards)}")
        print(f"Computer's final cards: {comp_cards}, score: {sum(comp_cards)}")

        if sum(players_cards) > 21:
            print("You lose")
        elif sum(comp_cards) > 21:
            print("You win")
        elif sum(players_cards) > sum(comp_cards):
            print("You win")
        elif sum(players_cards) == sum(comp_cards):
                print("Draw!")
        else:
            print("You lose")
    
    else:
        quit()

    blackjack()


blackjack()