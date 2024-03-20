# main.py
# Written by: Sofia Perez de Tudela
# 
# This class is what's called to get the TMGE started
# Has some command line displays and will call other classes
# in run()

import player
import tetris
import bejeweled

# Helper function to print the number of options
def _print_options(num : int) -> None:
    for i in range(1, num+1, 4):
        print(f"    {i}, ", end = '')
        for j in range(i+1, i+4 if i+4 < num+1 else num+1):
            print(f" {j}", end = '')
    print("\n   > ", end = "")

# Helper function to print num of player logins
# Returns a list of names
def _print_player_logins(num : int) -> list:
    players = []
    for i in range(1, num+1):
        print(f'Player {i}, enter your name here:\n  > ', end = '')
        name = input()

        while(name in players):
            print("That name is unavailable")
            print(f'Player {i}, enter your name here:\n  > ', end = '')
            name = input()
        
        players.append(name)
    return players

def login() -> None:
    print('Welcome to the TMGE')

    print('Please select the number of players from the options:')
    _print_options(2)
     # For now we're only accepting 2 player games
     # So any number not representing 2 will be rejected
    num_players = input()
 
    # Loop through invalid input, this condition might change
    while(num_players != "2" and num_players != "1"):
        print('Please select the number of players from the options:')
        _print_options(2)
        num_players = input()
    
    print("")
    player_names = _print_player_logins(int(num_players))
    players = [player.Player(name) for name in player_names]

    return players


# Maybe we'll have a GUI here
def display_games(games : list) -> None:
    print("\nAvailable Games")
    for i in range(len(games)):
        print(f"    {i+1}) {games[i].CLASS_NAME}")
    print("")

# Should return a game object at some point
def select_game(num_games) -> str:
    print("Please enter the number of the game you'd like to play: \n   > ", end = '')
    game = input()

    while (not game.isdigit()) or (int(game) not in range(1,num_games+1)):
        print("Please enter the number of the game you'd like to play: \n   > ", end = '')
        game = input()
    print("")
    return game

def run():
    # If you're adding a new game, put the class name here
    games = [tetris.Tetris, bejeweled.Bejeweled] 

    players = login()
    display_games(games)
    game_selection = select_game(len(games))

    game = games[int(game_selection)-1](players)

    game.runGame()

if __name__ == "__main__":
    run()