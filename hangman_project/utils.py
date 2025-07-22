#!/usr/bin/python3
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def is_valid_guess(guess):
    return len(guess) == 1 and guess.isalpha()

def print_game_state(word, guessed_letters, remaining_attempts):
    print(f"Word: {display_word(word, guessed_letters)}")
    print(f"Guessed Letters: {' '.join(sorted(guessed_letters))}")
    print(f"Remaining Attempts: {remaining_attempts}")
