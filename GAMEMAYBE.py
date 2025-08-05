#!/usr/bin/python3
# game.py

import random
from utils import display_word, is_valid_guess, print_game_state

def load_words(filename="wordlist.txt"):
    with open(filename, "r") as f:
        return [line.strip() for line in f if line.strip()]

def play_game():
    words = load_words()
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")

    while attempts > 0:
        print_game_state(word, guessed_letters, attempts)
        guess = input("Guess a letter: ").lower()

        if not is_valid_guess(guess):
            print("Invalid input. Please enter a single alphabetical letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print("Wrong guess!")

        if all(letter in guessed_letters for letter in word):
            print(f"\n🎉 Congratulations! You guessed the word: {word}")
            return

    print(f"\n💀 Game Over! The word was: {word}")
