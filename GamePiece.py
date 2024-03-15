from Color import Color

class GamePiece:
    def  __init__(self, color : Color) -> None:
        self.color = color

    def getPieceType(self):
        return self.color

    def getPieceStr(self):
        return self.color.name.lower()
     