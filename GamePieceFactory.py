from Color import Color
from GamePiece import GamePiece

# no longer needed
class GamePieceFactory:
    def createGamePiece(c : Color):
        '''
        Returns a newly created GamePiece to be placed in the board.
        '''
        return GamePiece(c)