

class GridSquare:
    is_empty = False
    piece = None
    location = [0,0]
    def __init__(self, x, y) -> None:
        self.location = [x,y]

    def removePiece(self):
        self.piece = None

    def changePiece(self, piece_to_change):
        self.piece = piece_to_change
