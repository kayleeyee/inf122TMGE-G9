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
        "Z" : "WHITE" 
    }
    
    GAME_NAME = 'Tetris'
    TETRIS_ROWS = 10
    TETRIS_COLS = 5
    
    END_GAME_SCORE = 300

    piece_keys = list(pieces.keys())
    last_move = None
    
    #grid = None

    def __init__(self, players) -> None:
        print("Tetris Innit")
        self.grid = Grid(self.TETRIS_ROWS, self.TETRIS_COLS)
        
        self.players = players
        self.current_piece_key = None
        self.current_piece = None
        self.current_piece_color = None
        self.current_piece_start_row = 0
        self.current_piece_start_col = 0
        
        self.current_player_index = 0
        
        self.runGameLoop()
    
    #def start(self):
        #self.runGameLoop()
        
    def populate_initial_grid(self):
        self.addNewPieces()
    
    def addNewPieces(self):
        #initialize a piece and change all the current_piece variables
        piece, piece_key, start_row, start_col = self._choose_new_pieces()
        self.current_piece = piece
        self.current_piece_key = piece_key
        self.current_piece_color = self.color_pieces[self.current_piece_key]
        self.current_piece_start_row = 0
        self.current_piece_start_col = (self.TETRIS_COLS - len(self.current_piece[0])) // 2
        
        #add new piece to grid
        if(not self._check_collison(self.current_piece, self.grid, self.current_piece_start_row, self.current_piece_start_col)):
            for row in range(len(piece)):
                for col in range(len(piece[row])):
                    if piece[row][col] == 1:           
                        self.grid.matrix[start_row + row][start_col + col] = Color(self.current_piece_color)

        self.tetris_testing_matrix()  
    
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
        if (not self._check_collison(rotated_piece, temp_grid, self.current_piece_start_row, new_start_col)):
            for row in range(len(rotated_piece)):
                for col in range(len(rotated_piece[row])):
                    if rotated_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][new_start_col + col] = Color(self.current_piece_color)
            self.grid = temp_grid

            self.current_piece = rotated_piece
            self.current_piece_start_col = new_start_col

        self.last_move = "rotate"
        self.tetris_testing_matrix()  
    
    def _move_down(self):
        temp_grid = copy.deepcopy(self.grid)
        

        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("COLORLESS")
                    
        while ((self.current_piece_start_row + 1 <= (self.TETRIS_ROWS - len(self.current_piece))) and (not self._check_collison(self.current_piece, temp_grid, self.current_piece_start_row + 1, self.current_piece_start_col))):
            self.current_piece_start_row += 1
        
        for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color(self.current_piece_color)
        
        self.grid = temp_grid
        self.last_move = "down"

        #self.checkMatch()
        self.tetris_testing_matrix()  

    def _move_left(self):
        temp_grid = copy.deepcopy(self.grid)

        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("COLORLESS")
                    
        if (((self.current_piece_start_col - 1) >= 0) and (not self._check_collison(self.current_piece, temp_grid, self.current_piece_start_row, self.current_piece_start_col - 1))): #??
            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col - 1 + col] = Color(self.current_piece_color)
            self.grid = temp_grid
            self.current_piece_start_col -= 1
        self.last_move = "left"
        self.tetris_testing_matrix()  

    def _move_right(self):
        temp_grid = copy.deepcopy(self.grid)

        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("COLORLESS")
        
        if ((self.current_piece_start_col + 1 <= (self.TETRIS_COLS - len(self.current_piece[0]))) and not self._check_collison(self.current_piece, temp_grid, self.current_piece_start_row, self.current_piece_start_col + 1)): #??
            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + 1 + col] = Color(self.current_piece_color)
            self.grid = temp_grid
            self.current_piece_start_col += 1
        self.last_move = "right"
        self.tetris_testing_matrix()  

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
        '''if (self._check_score_complete or self._check_collison):
            self.current_player_index += 1
            return True
        
        return False'''
        return False
            

    def _check_collison(self, new_piece, grid, start_row, start_col) -> bool:
        # can be used for check end game or any other move that need to check collision
        #print(new_piece)
        for row in range(len(new_piece)):
            for col in range(len(new_piece[row])):
                if (grid.return_grid()[start_row + row][start_col + col] != Color("COLORLESS") and new_piece[row][col] == 1):
                    return True
        return False
    
    def _check_score_complete(self) -> bool:
        return self.players[self.current_player_index].score >= self.END_GAME_SCORE

    def processUserInput(self, user_input):
        match user_input:
            case 'w':
                self._rotate()
            case 's':
                self._move_down()
            case 'd':
                self._move_right()
            case 'a':
                self._move_left()
            case _:
                print("Not a Valid Input Please only type: w, s, d or a")
            

    def checkMatch(self):
        #add list of rows' index to delete

        #Testing
        '''print("\n THIS IS THE CURRENT PIECE SELECTED:")
        print(self.current_piece_color)
        print(self.current_piece_key)
        print("THIS IS THE LAST MOVE MADE:")
        print(self.last_move)'''
        #Testing
        rows_to_delete = []
        
        for row in range(self.TETRIS_ROWS):
            row_all_color = True
            for col in range(self.TETRIS_COLS):
                if self.grid.return_grid()[row][col] == Color("COLORLESS"):
                    row_all_color = False
                    break   
            if row_all_color:
                rows_to_delete.append(row)
        
        #if there are row(s) to delete, empty the row
        if len(rows_to_delete) != 0: 

            #print("HERE ARE THE ROWS TO DELETE: ")
            #print(rows_to_delete)      
            rows_kept= []
            for row in range(self.TETRIS_ROWS):
                if row not in rows_to_delete:
                    rows_kept.append(self.grid.return_grid()[row])

            
            
            empty_rows = []
            for empty_row  in range(len(rows_to_delete)):
                columns_of_row = []
                for col in range(self.TETRIS_COLS):
                    columns_of_row.append(Color("COLORLESS"))
                empty_rows.append(columns_of_row)
            
            self.grid.matrix = empty_rows+rows_kept

            self.players[self.current_player_index].add_to_score(len(rows_to_delete)*10)
            
        if self.last_move == "down":
            self.addNewPieces()
        
        #add new piece after checking
        '''This will create a new piece after every move given the implementation of the game loop
        We will either need to find a way to keep track of when a piece is still in play to not create a new one, or see if we can change
        the game loop implementation so that it does not check match after every user_input'''
         
        # self.addNewPieces()
        self.tetris_testing_matrix() 

    def tetris_testing_matrix(self):
        for row in range(self.TETRIS_ROWS):
            for col in range(self.TETRIS_COLS):
                print(("| " + Color(self.grid.matrix[row][col]).value + " |").center(15), end="")
            print("\n ____________________________________________________________________________")
        print("\n")
        print("\n")
