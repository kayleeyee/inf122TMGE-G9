from Grid import Grid
from game import Game
from Color import Color
from player import Player
from TetrisGridGUI import TetrisGridGUI

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
        "T" : "ORANGE",
        "Z" : "WHITE" 
    }
    
    GAME_NAME = 'Tetris'
    TETRIS_ROWS = 20
    TETRIS_COLS = 10
    
    END_GAME_SCORE = 30
    MATCH_SCORE = 10

    piece_keys = list(pieces.keys())
    last_move = None

    def __init__(self, players) -> None:
        self.grid = Grid(self.TETRIS_ROWS, self.TETRIS_COLS)
        
        self.players = players
        self.current_piece_key = None
        self.current_piece = None
        self.current_piece_color = None
        self.current_piece_start_row = 0
        self.current_piece_start_col = 0
        
        self.current_player_index = 0
    
    def printInstructions(self):
        '''
        Prints instructions on how to play Tetris to the player's terminal
        '''
        instructions = 'Welcome to Bejeweled!\nTo play this game, use "w/a/s/d" to rotate/move left/move right/move down\nMove down will move the piece all the way down'
        print(instructions)
    
    def displayPlayerScore(self):
        print(f"{self.players[self.current_player_index].getName()}'s score: {self.players[self.current_player_index].getScore()}")
        
    def populateInitialGrid(self):
        '''
        Tetris's grid initialize
        Add the first tetris piece to the grid
        '''
        self.addNewPieces()
        
    def addNewPieces(self)->bool:
        #initialize a piece
        piece, piece_key, start_row, start_col = self._choose_new_pieces()
        
        #add new piece to grid
        if(not self._check_collison(piece, self.grid, start_row, start_col)):
            # change all the current_piece variables
            self.current_piece = piece
            self.current_piece_key = piece_key
            self.current_piece_color = self.color_pieces[self.current_piece_key]
            self.current_piece_start_row = start_row
            self.current_piece_start_col = start_col
            
            for row in range(len(piece)):
                for col in range(len(piece[row])):
                    if piece[row][col] == 1:           
                        self.grid.matrix[start_row + row][start_col + col] = Color(self.current_piece_color)
            return True 

        return False
    
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
 
    def endGame(self) -> bool:
        '''
        Check when to end game. Game is done when player's index is over the number of players
        '''
        if self.current_player_index >= len(self.players):
            return True
        return False
    
    def checkMatch(self):
        '''
        If the piece is gone down, check for row(s) that are filled with colors and remove the row(s)
        '''
        rows_to_delete = []
        
        for row in range(self.TETRIS_ROWS):
            row_all_color = True
            for col in range(self.TETRIS_COLS):
                if self.grid.return_grid()[row][col] == Color("BLACK"):
                    row_all_color = False
                    break   
            if row_all_color:
                rows_to_delete.append(row)
        
        #if there are row(s) to delete, empty the row
        if len(rows_to_delete) != 0: 

            self.players[self.current_player_index].addToScore(len(rows_to_delete)*10)
            
            rows_kept= []
            for row in range(self.TETRIS_ROWS):
                if row not in rows_to_delete:
                    rows_kept.append(self.grid.return_grid()[row])

            empty_rows = []
            for empty_row  in range(len(rows_to_delete)):
                columns_of_row = []
                for col in range(self.TETRIS_COLS):
                    columns_of_row.append(Color("BLACK"))
                empty_rows.append(columns_of_row)
            
            self.grid.matrix = empty_rows+rows_kept

            self.players[self.current_player_index].addToScore(len(rows_to_delete)*10)

        if self.last_move == "down":
            self._handle_player()
        
    def _handle_player(self):
        '''
        Increase the index of current_player_index if the current player's game is finished
        '''
        if self.addNewPieces() == False or self._check_score_complete():
                self.current_player_index += 1
                self.grid = Grid(self.TETRIS_ROWS, self.TETRIS_COLS)
                self.populate_initial_grid()
    
    def _rotate(self):
        '''
        Rotate the piece when "w" is pressed
        '''
        rotated_piece = list(zip(*self.current_piece[::-1]))
        new_start_col = (self.TETRIS_COLS - len(rotated_piece[0])) // 2

        #temporary board to check for collision for new piece
        temp_grid = copy.deepcopy(self.grid)

        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("BLACK")
        
        #if there is not collision, apply change to the piece
        if (not self._check_collison(rotated_piece, temp_grid, self.current_piece_start_row, new_start_col)):
            for row in range(len(rotated_piece)):
                for col in range(len(rotated_piece[row])):
                    if rotated_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][new_start_col + col] = Color(self.current_piece_color)
            self.grid = temp_grid

            self.current_piece = rotated_piece
            self.current_piece_start_col = new_start_col

        self.last_move = "rotate" 
    
    def _move_down(self):
        '''
        Move the piece all the way down when "s" is pressed
        '''
        temp_grid = copy.deepcopy(self.grid)
        
        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("BLACK")
                    
        while ((self.current_piece_start_row + 1 <= (self.TETRIS_ROWS - len(self.current_piece))) and (not self._check_collison(self.current_piece, temp_grid, self.current_piece_start_row + 1, self.current_piece_start_col))):
            self.current_piece_start_row += 1
        
        for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color(self.current_piece_color)
        
        self.grid = temp_grid
        self.last_move = "down"
        self.checkMatch()

    def _move_left(self):
        '''
        Move the piece to the left by one column when "a" is pressed
        '''
        temp_grid = copy.deepcopy(self.grid)

        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("BLACK")
                    
        if (((self.current_piece_start_col - 1) >= 0) and (not self._check_collison(self.current_piece, temp_grid, self.current_piece_start_row, self.current_piece_start_col - 1))): #??
            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col - 1 + col] = Color(self.current_piece_color)
            self.grid = temp_grid
            self.current_piece_start_col -= 1
        
        self.last_move = "left"

    def _move_right(self):
        '''
        Move the piece to the right by one column when "d" is pressed
        '''
        temp_grid = copy.deepcopy(self.grid)

        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = Color("BLACK")
        
        if ((self.current_piece_start_col + 1 <= (self.TETRIS_COLS - len(self.current_piece[0]))) and not self._check_collison(self.current_piece, temp_grid, self.current_piece_start_row, self.current_piece_start_col + 1)): #??
            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + 1 + col] = Color(self.current_piece_color)
            self.grid = temp_grid
            self.current_piece_start_col += 1
        
        self.last_move = "right"

    def _choose_new_pieces(self):
        '''
        Randomize piece choice for addNewPieces method
        '''
        new_piece_key = random.choice(self.piece_keys)
        new_piece = self.pieces[new_piece_key]

        start_row = 0
        start_col = (self.TETRIS_COLS - len(new_piece[0])) // 2

        return new_piece, new_piece_key, start_row, start_col 
    
    def _check_collison(self, new_piece, grid, start_row, start_col) -> bool:
        '''
        Check if the piece collide with the grid or any other pieces.
        '''
        for row in range(len(new_piece)):
            for col in range(len(new_piece[row])):
                if (grid.return_grid()[start_row + row][start_col + col] != Color("BLACK") and new_piece[row][col] == 1):
                    return True
        return False
    
    def _check_score_complete(self) -> bool:
        '''
        Check if the current player has reached a certain score
        '''
        return self.players[self.current_player_index].score >= self.END_GAME_SCORE

    # def tetris_testing_matrix(self):
    #     for row in range(self.TETRIS_ROWS):
    #         for col in range(self.TETRIS_COLS):
    #             print(("| " + Color(self.grid.matrix[row][col]).value + " |").center(15), end="")
    #         print("\n ____________________________________________________________________________")
    #     print("\n")
    #     print("\n")
    
    def printGrid(self):
        for r in range(self.TETRIS_ROWS):
            new_row = []
            for c in range(self.TETRIS_COLS):
                new_row.append(self.grid.matrix[r][c].name)
            print(new_row)

    def makeLower(self):
        new_matrix = []

        for row in range(self.TETRIS_ROWS):
            row_matrix =  []
            for column in range(self.TETRIS_COLS):
                # print(self.grid.matrix[row][column].name.lower())
                row_matrix.append(self.grid.matrix[row][column].name.lower())
            new_matrix.append(row_matrix)
        # print(new_matrix)
        return new_matrix
    
if __name__ == "__main__":
    players = [Player('p1'), Player('p2')]
    tetris = Tetris(players)
    tetris.populateInitialGrid()
    gui = TetrisGridGUI(tetris.makeLower(), tetris)
    gui.run()