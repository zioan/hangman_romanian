import random
import os
from words import word_list
from art import stages, logo


def play_game():
    os.system('cls')
    game_over = False
    chosen_word = random.choice(word_list)
    word_length = len(chosen_word)
    lives = 6

    print(logo)
    # print(chosen_word)

    def game_restart():
        os.system("py main.py")

    display = []
    for letter in range(word_length):
        display += '_'

    print(display)
    print(f"Cuvantul are: {word_length} litere")

    while not game_over:
        guess = input("Ghiceste o litera: ").lower()

        if guess in display:
            print(f"Ai ghicit deja: {guess}")

        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter

        if guess not in chosen_word:
            print(f"{guess} NU este in cuvant.")
            lives -= 1
            if lives == 0:
                game_over = True
                print("Game over. Ai pierdut!")
                print(f"Cuvantul corect este: {chosen_word}")
                game_restart()

        if "_" not in display:
            game_over = True
            print("Ai castigat!")
            print(f"Corect, cuvantul era: {chosen_word}")
            while input("Joc nou? ( y / n): ") == 'y':
                game_restart()

        print(stages[lives])
        word = ' '.join(display)
        print(word)


while True:
    play_game()
