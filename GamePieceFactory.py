from Color import Color
from GamePiece import GamePiece

class GamePieceFactory:
    def createGamePiece(c : Color):
        '''
        Returns a newly created GamePiece to be placed in the board.
        '''
        return GamePiece(c)