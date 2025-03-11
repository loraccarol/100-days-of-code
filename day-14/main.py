from game_data import data
import random
from os import system

def get_entity_data(index_id):
    return data[index_id]

def get_entity_description(index_id):
    entity = data[index_id]
    return f"{entity["name"]}, a {entity["description"]}, from {entity["country"]}"

def most_followed(a, b):
    right = {}

    print(f"Compare A: {get_entity_description(a)}")
    print("VS.")
    print(f"Compare B: {get_entity_description(b)}")

    if get_entity_data(a)["follower_count"] > get_entity_data(b)["follower_count"]:
        right = {"answer":"a", "value":a}
    else:
        right = {"answer":"b", "value":b}
        
    return right

def game():
    continue_playing = True
    score = 0

    op_a = random.randint(0, len(data))
    while continue_playing:
        op_b = random.randint(0, len(data))

        right_answer = most_followed(op_a, op_b)
        answer = input("Who has more followers? Type 'a' or 'b'. ").lower()

        if answer == right_answer["answer"]:
            score += 1
            system("cls")
            print(f"You are right. Current score: {score}")
            op_a = right_answer["value"]
        else:
            print(f"You are wrong. Final score: {score}")
            continue_playing = False

game()