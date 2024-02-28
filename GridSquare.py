from collections import namedtuple
Coordinate = namedtuple('Coordinate', ['x', 'y'])

class GridSquare:
    is_empty = False
    piece = None
    location = None
    def __init__(self, x, y) -> None:
        self.location = Coordinate(x, y)

    def removePiece(self):
        self.piece = None

    def changePiece(self, piece_to_change):
        self.piece = piece_to_change


