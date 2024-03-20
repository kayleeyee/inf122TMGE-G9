from GamePiece import GamePiece
from GamePieceFactory import GamePieceFactory as GPF
from Color import Color


class Grid:
    def __init__(self, rows, columns) -> None:
        self.matrix = []
        self.create_grid(rows, columns)
    
    def create_grid(self, rows, columns) -> None:
        for row in range(rows):
            row_matrix =  []
            for column in range(columns):
                row_matrix.append(GPF.createGamePiece(Color.BLACK)) 
            self.matrix.append(row_matrix)

    def return_grid(self):
        return self.matrix
    
    # used for debugging
    def display(self) -> None:
        print(self.matrix)
    

    def getCols(self):
        return len(self.matrix[0])


    def getRows(self):
        return len(self.matrix)
    



    
