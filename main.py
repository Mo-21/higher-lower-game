from game_data import data
import random

print("Hello to this stupid game. I don't know what we are going to do, just assume you're enjoying.\n")
start = input('Write "start" to start playing, obviously.\n')


def generate_random_number():
    return random.randint(0, 49)


def game_board():

    has_More_followers = ""
    current_person = ""
    score = 0
    is_playing = True

    while is_playing:
        if score == 0:
            random_number_A = generate_random_number()
            random_number_B = generate_random_number()
            person_A = data[random_number_A]
            person_B = data[random_number_B]
        elif score > 0:
            random_number_A = generate_random_number()
            random_number_B = generate_random_number()
            person_A = current_person
            person_B = data[random_number_B]

        if person_A["follower_count"] > person_B["follower_count"]:
            has_More_followers = "A"
            current_person = person_A
        else:
            has_More_followers = "B"
            current_person = person_B

        print(
            f'Compare A: {person_A["name"]}, a {person_A["description"]}, from {person_A["country"]}\n\n')
        print("VS.\n\n")
        print(
            f'Compare B: {person_B["name"]}, a {person_B["description"]}, from {person_B["country"]}\n')

        answer = input("Who has more followers? Type A or B:  ")

        if answer == has_More_followers:
            score += 1
            print(f"Correct Your score is: {score}\n")
        else:
            score = 0
            is_playing = False
            return print("Naahh, not this time.")


if start == "start":
    game_board()
