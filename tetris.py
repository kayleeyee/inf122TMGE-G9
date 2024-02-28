from Grid import Grid
from game import Game

class Tetris(Game):
    GAME_NAME = 'Tetris'
    TETRIS_ROWS = 10
    TETRIS_COLS = 20

    grid = None

    def __init__(self, game_name, players) -> None:
        super.__init__(self, self.GAME_NAME, players)
        self.grid = Grid(self.TETRIS_ROWS, self.TETRIS_COLS)

    def addNewPieces(self):
        pass