from Grid import Grid
from game import Game
from Color import Color
import random

class Tetris(Game):
    GAME_NAME = 'Tetris'
    TETRIS_ROWS = 10
    TETRIS_COLS = 20

    #grid = None

    def __init__(self, players) -> None:
        super().__init__(self.TETRIS_ROWS, self.TETRIS_COLS, self.GAME_NAME, players)
        print("Tetris Innit")
        self.runGameLoop()
        
    def populate_initial_grid(self):
        print("Populate_initial_grid")
        print(self.grid.return_grid()[0][0])
    
    def addNewPieces(self):
        piece_keys = list(pieces.keys())

        new_piece_key = random.choice(piece_keys)
        new_piece = pieces[new_piece_key]

        start_row = 0
        start_col = (self.TETRIS_COLS - len(new_piece[0])) // 2
        
        for row in range(len(new_piece)):
            for col in range(len(new_piece[row])):
                # check for end game first before adding
                if (self.grid[start_row + row][start_col + col] != Color("COLORLESS") and new_piece[row][col] == 1):
                    #end the game
                    break
                
        #if not end game, add the piece :D, this is simple one??
        for row in range(len(new_piece)):
            for col in range(len(new_piece[row])):
                if new_piece[row][col] == 1:           
                    self.grid[start_row + row][start_col + col] = color_pieces[new_piece_key]            



    def takeUserInput(self):
        pass

    def endGame(self) -> bool:
        pass

    def processUserInput(self, user_input):
        #print("Process User Input")
        pass

    def checkMatch(self):
        #for row in range(len(self.grid)):
         #   for column in range(len(self.grid[row])):
         #       if self.grid[row][column].is_empty == False: #?
          #          return
                
            #...
        for row in range(len(self.TETRIS_ROWS)):
            for col in range(len(self.TETRIS_COLS)):
                pass

pieces = {
    "I": [
        [1, 1, 1, 1] #may expand to accomodate rotation Ex: [[0, 0, 0, 1],
                                                        #   [0, 0, 0, 1],
                                                        #   [0, 0, 0, 1],
                                                        #   [0, 0, 0, 1]]
    ],
    "L": [
        [1, 0, 0],
        [1, 1, 1]
    ],
    "J": [
        [0, 0, 1],
        [1, 1, 1]
    ],
    "O": [
        [1, 1],
        [1, 1]
    ],
    "S": [
        [0, 1, 1],
        [1, 1, 0]
    ],
    "T": [
        [0, 1, 0],
        [1, 1, 1]
    ],
    "Z": [
        [1, 1, 0],
        [0, 1, 1]
    ]
}

color_pieces = {
    "I" : "RED",
    "L" : "BLUE",
    "J" : "YELLOW",
    "O" : "PURPLE",
    "S" : "GREEN",
    "T" : "PINK",
    "Z" : "GREY" 
}
