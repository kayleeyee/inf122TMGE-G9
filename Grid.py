from GridSquare import GridSquare


class Grid:
    matrix = []
    def __init__(self, rows, columns) -> None:
        self.create_grid(rows, columns)
    
    def create_grid(self, rows, columns) -> None:
        for row in rows:
            for column in columns:
                self.matrix.append(GridSquare(row, column))

    def display(self) -> None:
        print(self.matrix)


    def update(self) -> None:
        pass
    
        


    
