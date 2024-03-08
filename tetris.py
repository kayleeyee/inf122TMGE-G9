from Grid import Grid
from game import Game
from Color import Color
import random
import copy

class Tetris(Game):
    pieces = {
    "I": [[1, 1, 1, 1]],
    "L": [[1, 0, 0],
        [1, 1, 1]],
    "J": [[0, 0, 1],
        [1, 1, 1]],
    "O": [[1, 1],
        [1, 1]],
    "S": [[0, 1, 1],
        [1, 1, 0]],
    "T": [[0, 1, 0],
          [1, 1, 1]],
    "Z": [[1, 1, 0],
        [0, 1, 1]]
    }

    color_pieces = {
        "I" : "RED",
        "L" : "BLUE",
        "J" : "YELLOW",
        "O" : "PURPLE",
        "S" : "GREEN",
        "T" : "PINK",
        "Z" : "GREY" 
    }
    
    GAME_NAME = 'Tetris'
    TETRIS_ROWS = 10
    TETRIS_COLS = 20

    current_piece_key = None
    current_piece = None
    current_piece_color = None
    current_piece_start_row = 0
    current_piece_start_col = 0
    
    
    piece_keys = list(pieces.keys())

    grid = Grid(TETRIS_ROWS, TETRIS_COLS)
    
    #grid = None

    def __init__(self, players) -> None:
        print("Tetris Innit")
        self.runGameLoop()
        
    def populate_initial_grid(self):
        self.addNewPieces()
    
    def addNewPieces(self):
        piece, piece_key, start_row, start_col = self._choose_new_pieces()
        self.current_piece = piece
        self.current_piece_key = piece_key
        self.current_piece_color = self.color_pieces[self.current_piece_key]
        self.current_piece_start_row = start_row
        self.current_piece_start_col = start_col

        if (self.endGame != False):    
        #if not end game, add the piece :D, this is simple one??
            for row in range(len(piece)):
                for col in range(len(piece[row])):
                    if piece[row][col] == 1:           
                        self.grid.matrix[start_row + row][start_col + col] = Color(self.current_piece_color)   
    
    def _rotate(self):
        #modify the piece's list and store in a variable
        rotated_piece = list(zip(*self.current_piece[::-1]))

        new_start_col = (self.TETRIS_COLS - len(rotated_piece[0])) // 2

        #temporary board to check for collision for new piece
        temp_grid = copy.deepcopy(self.grid)


        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("COLORLESS")
        
        #if there is not collision, rotate the piece
        if (self._check_collison(rotated_piece, temp_grid, self.current_piece_start_row, new_start_col) != True):
            for row in range(len(rotated_piece)):
                for col in range(len(rotated_piece[row])):
                    if rotated_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][new_start_col + col] = Color(self.current_piece_color)
            self.grid = temp_grid

            self.current_piece = rotated_piece
            self.current_piece_start_row = new_start_col
    
    def _move_down(self):
        while (self._check_collison(self.current_piece, self.grid, self.current_piece_start_col + 1, self.current_piece_start_row) != True): #??
            temp_row = self.current_piece_start_row + 1

            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        self.grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("COLORLESS")
                        self.grid.matrix[temp_row + row][self.current_piece_start_col + col] = Color(self.current_piece_color)
            
            start_row += 1

    def _move_left(self):
        if (self._check_collison(self.current_piece, self.grid, self.current_piece_start_row, self.current_piece_start_col - 1) != True): #??
            temp_col = self.current_piece_start_col - 1

            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        self.grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("COLORLESS")
                        self.grid.matrix[self.current_piece_start_row + row][temp_col + col] = Color(self.current_piece_color)
            
            self.current_piece_start_col -= 1

    def _move_right(self):
        if (self._check_collison(self.current_piece, self.grid, self.current_piece_start_row, self.current_piece_start_col + 1) != True): #??
            temp_col = self.current_piece_start_col + 1

            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        self.grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("COLORLESS")
                        self.grid.matrix[self.current_piece_start_row + row][temp_col + col] = Color(self.current_piece_color)
            
            self.current_piece_start_col += 1

    def _choose_new_pieces(self):
        new_piece_key = random.choice(self.piece_keys)
        new_piece = self.pieces[new_piece_key]

        start_row = 0
        start_col = (self.TETRIS_COLS - len(new_piece[0])) // 2

        return new_piece, new_piece_key, start_row, start_col

    def takeUserInput(self):
        pass
 
    def endGame(self) -> bool:
        #check collison and other way to end game
        pass

    def _check_collison(self, grid, new_piece, start_row, start_col) -> bool:
        # can be used for check end game or any other move that need to check collision
        for row in range(len(new_piece)):
            for col in range(len(new_piece[row])):
                if (grid[start_row + row][start_col + col] != Color("COLORLESS") and new_piece[row][col] == 1):
                    return True
        return False

    def processUserInput(self, user_input):
        #print("Process User Input")
        pass

    def checkMatch(self, start_col):
        #temp check
        for row in range(start_col, len(self.TETRIS_ROWS)):
            deleteRow = True
            temporaryGrid = self.grid.getMatrix()
            for col in range(len(self.TETRIS_COLS)):
                if self.grid[row][col] == Color("COLORLESS"):
                    deleteRow = False
            
            if deleteRow:
                slice1 = temporaryGrid[:row]
                slice2 = temporaryGrid[row+1:]

                grid = [[Color("COLORLESS") for _ in range(self.TETRIS_COLS)]] + slice1 + slice2 #??

