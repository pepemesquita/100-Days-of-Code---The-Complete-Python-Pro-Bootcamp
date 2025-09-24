import random as rd
from hangman_words import word_list
from hangman_art import stages, logo

print(logo)

lives = 6
error = False
won = False
chosen_word = rd.choice(word_list)
display = ["_"] * len(chosen_word)

print("".join(display))

while not won and lives >= 1:
    print(f"Life remaining: {lives}")
    chosen_letter = input("Type a letter: ").lower()

    error = True

    for i in range(len(chosen_word)):
        if chosen_word[i] == chosen_letter:
            display[i] = chosen_word[i]
            error = False

    if error:
        lives -= 1

    print("".join(display))

    if chosen_word == "".join(display):
        print("You won! Congrats!")
        won = True

    print(stages[lives])