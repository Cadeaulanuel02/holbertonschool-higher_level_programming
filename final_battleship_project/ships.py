#!/usr/bin/python3

import random
from config import SHIP_SPECS, BOARD_SIZE

class Ship:
    def __init__(self, length, positions=None):
        """
        Initializes a Ship object.
        
        Args:
            length (int): The length of the ship.
            positions (list of tuples): Coordinates occupied by the ship.
        """
        self.length = length
        self.positions = positions if positions else []
        self.hits = set()

    def register_hit(self, position):
        """
        Records a hit on the ship if the position matches.
        
        Args:
            position (tuple): (row, col) of the hit attempt.
        Returns:
            bool: True if it's a valid hit, False otherwise.
        """
        if position in self.positions:
            self.hits.add(position)
            return True
        return False

    def is_sunk(self):
        """Returns True if all ship positions have been hit."""
        return len(self.hits) >= self.length


def load_fleet():
    """
    Creates and returns a fresh fleet of ships 
    based on the lengths defined in SHIP_SPECS.
    
    Returns:
        list: A list of Ship instances with no positions yet.
    """
    fleet = []
    for length in SHIP_SPECS:
        ship = Ship(length, [])
        fleet.append(ship)
    return fleet


def place_ship_randomly(board, ship):
    """
    Randomly places a single ship on the board without overlap.
    
    Args:
        board (list[list[str]]): The game board.
        ship (Ship): The ship to place.
    """
    placed = False
    while not placed:
        orientation = random.choice(["H", "V"])  # Horizontal or Vertical
        
        if orientation == "H":
            row = random.randint(0, BOARD_SIZE - 1)
            col = random.randint(0, BOARD_SIZE - ship.length)
            
            # Check if cells are free
            if all(board[row][col + i] == "~" for i in range(ship.length)):
                for i in range(ship.length):
                    board[row][col + i] = "S"
                    ship.positions.append((row, col + i))
                placed = True
        
        else:  # Vertical
            row = random.randint(0, BOARD_SIZE - ship.length)
            col = random.randint(0, BOARD_SIZE - 1)
            
            if all(board[row + i][col] == "~" for i in range(ship.length)):
                for i in range(ship.length):
                    board[row + i][col] = "S"
                    ship.positions.append((row + i, col))
                placed = True


