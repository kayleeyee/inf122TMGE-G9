from Color import Color


class GamePiece:
    next_id = 0
    def  __init__(self, color : Color) -> None:
        self.id = self.next_id
        GamePiece.next_id += 1
        self.color = color

    def getID(self):
        return self.id

    def getColor(self):
        return self.color
     