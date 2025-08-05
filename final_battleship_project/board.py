#!/usr/bin/python3

from config import BOARD_SIZE

def print_headers():
    """Prints the column labels (1–BOARD_SIZE)."""
    print("  ", end="")
    for col in range(1, BOARD_SIZE + 1):
        print(f" {col} ", end="")
    print()

def print_board(board, hide_ships=False):
    """
    Prints the game board with row and column labels.
    If hide_ships=True, ship cells are shown as water (~).
    """
    print_headers()
    for row_idx, row in enumerate(board):
        print(chr(65 + row_idx), end=" ")  # Row label (A, B, ...)
        for cell in row:
            if hide_ships and cell == "S":  # Hide ships for opponent view
                print(" ~ ", end="")
            else:
                print(f" {cell} ", end="")
        print()  # Newline after each row




if __name__ == "__main__":
    # Sample 5x5 board
    sample_board = [
        ["~", "~", "S", "~", "~"],
        ["~", "O", "~", "~", "~"],
        ["S", "S", "~", "~", "~"],
        ["~", "~", "~", "X", "~"],
        ["~", "~", "~", "~", "~"]
    ]

    print("Player view (ships visible):")
    print_board(sample_board, hide_ships=False)

    print("\nOpponent view (ships hidden):")
    print_board(sample_board, hide_ships=True)
