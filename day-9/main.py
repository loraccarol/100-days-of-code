from os import system

print("Welcome")

bidders = {}

continue_bidding = True

while continue_bidding:
    name = input("What's your name? ")
    bid = int(input("What's your bid? $"))

    bidders[name] = bid

    another_bidder = input("Is there another bidder? 'yes' or 'no'. ").lower()
    if another_bidder == "no":
        continue_bidding = False
        
    system("cls")

highest_bid = {"name": '', "value": 0}
for bidder in bidders:
    if bidders[bidder] > highest_bid["value"]:
        highest_bid["name"] = bidder
        highest_bid["value"] = bidders[bidder]

print(f"The winner is {highest_bid['name']}, with the bid of ${highest_bid['value']}")