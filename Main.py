# main.py
# Written by: Sofia Perez de Tudela
# 
# This class is what's called to get the TMGE started
# Has some command line displays and will call other classes
# in run()

def login():
    print("Welcome to the TMGE: Please sign in here")

#Maybe we'll have a GUI here
def display_games():
    pass

def select_game():
    pass

def run():
    players = login()
    display_games()
    game = select_game()

if __name__ == "__main__":
    run()