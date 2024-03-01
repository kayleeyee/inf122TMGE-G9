from Grid import Grid
from game import Game

class Tetris(Game):
    GAME_NAME = 'Tetris'
    TETRIS_ROWS = 10
    TETRIS_COLS = 20

    grid = None

    def __init__(self, players) -> None:
        super.__init__(self, self.TETRIS_ROWS, self.TETRIS_COLS, self.GAME_NAME, players)

    def addNewPieces(self):
        pass
    
    def takeUserInput(self):
        pass

    def endGame(self) -> bool:
        pass

    def checkMatch(self):
        #for row in range(len(self.grid)):
         #   for column in range(len(self.grid[row])):
         #       if self.grid[row][column].is_empty == False: #?
          #          return
                
            #...
        pass
