from GridSquare import GridSquare
from Color import Color


class Grid:
    def __init__(self, rows, columns) -> None:
        self.matrix = []
        self.create_grid(rows, columns)
    
    def create_grid(self, rows, columns) -> None:
        for row in range(rows):
            row_matrix =  []
            for column in range(columns):
                row_matrix.append(Color("COLORLESS")) 
            self.matrix.append(row_matrix)
    
    def return_grid(self):
        return self.matrix
    
    
    def display(self) -> None:
        print(self.matrix)


    def update(self) -> None:
        pass
    

    def getCols(self):
        return len(self.matrix[0])


    def getRows(self):
        return len(self.matrix)
    
    
    def getMatrix(self):
        return self.matrix
        


    
