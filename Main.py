# main.py
# Written by: Sofia Perez de Tudela
# 
# This class is what's called to get the TMGE started
# Has some command line displays and will call other classes
# in run()

import player
from tetris import Tetris

def login() -> None:
    print('Welcome to the TMGE')
    print('Player 1, enter your name here: \n   > ', end = '')
    name1 = input()
    print('Player 2, enter your name here: \n   > ', end = '')
    name2 = input()

    return [player.Player(name1), player.Player(name2)]


# Maybe we'll have a GUI here
def display_games(games : list) -> None:
    print("\nAvailable Games")
    for i in range(len(games)):
        print(f"{i+1}) {games[i+1]}")

# Should return a game object at some point
def select_game() -> str:
    print("Please enter the number of the game you'd like to play: \n   > ", end = '')
    game = input()
    
    return game

def run():
    # For now this is an array of str, might make game obj possibly
    #games = ["Tetris", "Bejeweled"] 

    #players = login()
    #display_games(games)
    print("Main")
    game = Tetris([player.Player("1"), player.Player("2")])

    # Maybe we could do something like
    # new_game = Game(game)
    # new_game.start() ??
    # This moreso depends on how we decide to implement it tho

if __name__ == "__main__":
    run()