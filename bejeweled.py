from Grid import Grid
from game import Game

class Bejeweled(Game) :
    GAME_NAME = 'Bejeweled'
    BEJEWELED_ROWS = 8
    BEJEWELED_COLS = 8

    def __init__(self, players):
        super.__init__(self, self.BEJEWELED_ROWS, self.BEJEWELED_COLS, self.GAME_NAME, players)
        # create board for game here ~ clear any matches beforehand until no more ?
        # have a preset board? "Levels"

    def addNewPieces(self):
        # checks every grid square, if the grid square is empty, fill it with a new piece
        pass

    def endGame(self):
        pass

    def checkMatch(self):
        '''

        '''
        pass