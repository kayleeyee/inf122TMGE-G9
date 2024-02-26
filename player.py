# player.py
# Written by: Sofia Perez de Tudela
#
# This class contains the class def for players
# Players hold their name and score
# The score will be changed by the Game class

class Player():

    # Initialize with username, and a score of 0
    def __init__(self, name : str):
        self.username = name
        self.score = 0

    # Increase or decrease the score
    def add_to_score(self, num : int) -> None:
        self.score += num