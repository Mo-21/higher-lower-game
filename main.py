from game_data import data
import random

print("Hello to this stupid game. I don't know what we are going to do, just assume you're enjoying.\n")
start = input('Write "start" to start playing, obviously.\n')


def generate_random_number():
    return random.randint(0, 49)


def game_board():
    random_number_A = generate_random_number()
    random_number_B = generate_random_number()
    person_A = data[random_number_A]
    person_B = data[random_number_B]
    has_More_followers = ""

    if person_A["follower_count"] > person_B["follower_count"]:
        has_More_followers = "A"
    else:
        has_More_followers = "B"

    print(
        f'Compare A: {data[random_number_A]["name"]}, a {data[random_number_A]["description"]}, from {data[random_number_A]["country"]}\n\n')
    print("VS.\n\n")
    print(
        f'Compare B: {data[random_number_B]["name"]}, a {data[random_number_B]["description"]}, from {data[random_number_B]["country"]}\n')

    answer = input("Who has more followers? Type A or B:  ")

    if answer == has_More_followers:
        print("Correct")
    else:
        print("Naahh, not this time.")


if start == "start":
    game_board()
