from Color import Color


class GamePiece:
    def  __init__(self, next_id, string_color) -> None:
        self.id = next_id
        self.next_id = next_id+1
        self.color = Color(string_color)

     