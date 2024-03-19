from Grid import Grid
from game import Game
from Color import Color
from player import Player
from TetrisGridGUI import TetrisGridGUI
from GamePiece import GamePiece
from GamePieceFactory import GamePieceFactory as GPF
import MatchStrategy as MS

import random
import copy

from collections import namedtuple
Coordinate = namedtuple('Coordinate', ['x', 'y'])

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
        "I" : GPF.createGamePiece(Color("RED")),
        "L" : GPF.createGamePiece(Color("BLUE")),
        "J" : GPF.createGamePiece(Color("YELLOW")),
        "O" : GPF.createGamePiece(Color("PURPLE")),
        "S" : GPF.createGamePiece(Color("GREEN")),
        "T" : GPF.createGamePiece(Color("ORANGE")),
        "Z" : GPF.createGamePiece(Color("WHITE")),
        "EMPTY": GPF.createGamePiece(Color("BLACK"))
    }
    
    TETRIS_HORIZONTAL_MATCH = MS.HorizontalMatchStrategy()
    GAME_NAME = 'Tetris'
    TETRIS_ROWS = 20
    TETRIS_COLS = 10
    
    END_GAME_SCORE = 100
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
        print(self.players[self.current_player_index])
        
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
            
            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:           
                        self.grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = self.current_piece_color
            # self.tetris_testing_matrix()
            return True 

        return False
    
    def processUserInput(self, user_input):
        if user_input == 'w':
            self._rotate()
        elif user_input == 's':
            self._move_down()
        elif user_input == 'd':
            self._move_right()
        elif user_input ==  'a':
            self._move_left()
        else:
            print("Not a Valid Input Please only type: w, s, d or a")
 
    def endGame(self) -> bool:
        '''
        Check when to end game. Game is done when player's index is over the number of players
        '''
        self.gui.window.destroy()
        #exit()
    
    def checkMatch(self):
        '''
        If the piece is gone down, check for row(s) that are filled with colors and remove the row(s)
        '''
        coord_list = [Coordinate(self.current_piece_start_row, 0), Coordinate(self.TETRIS_ROWS, self.TETRIS_COLS)]
        coord_to_delete = self.TETRIS_HORIZONTAL_MATCH.match(self.grid, coord_list)
        
        if (coord_to_delete != None):
            rows_to_delete = [coord.x for coord in coord_to_delete]
            
            #if there are row(s) to delete, empty the row
            if len(rows_to_delete) != 0:
                self._remove_and_add_rows(rows_to_delete)
                self.players[self.current_player_index].addToScore(len(rows_to_delete)*10)

        self.displayPlayerScore()
        
        if self.last_move == "down":
            self._handle_move_down()
    
    def _remove_and_add_rows(self, rows_to_delete):
        rows_kept= []
        for row in range(self.TETRIS_ROWS):
            if row not in rows_to_delete:
                rows_kept.append(self.grid.return_grid()[row])
        
        empty_rows = []
        new_row = [self.color_pieces["EMPTY"] for _ in range(self.TETRIS_COLS)]
        for _ in range(len(rows_to_delete)):
            empty_rows.append(new_row)
        
        self.grid.matrix = empty_rows+rows_kept
       
    def _handle_move_down(self):
        '''
        Increase the index of current_player_index if the current player's game is finished
        '''
        if self.addNewPieces() == False or self._check_score_complete():
            self.current_player_index += 1
            if(self.current_player_index < len(self.players)):
                self.grid = Grid(self.TETRIS_ROWS, self.TETRIS_COLS)
                self.populateInitialGrid()
            else:
                self.endGame()
    
    def _rotate(self):
        '''
        Rotate the piece when "w" is pressed
        '''
        rotated_piece = list(zip(*self.current_piece[::-1]))
        
        center_col = len(self.current_piece[0]) // 2
        new_start_col = self.current_piece_start_col + center_col - len(rotated_piece[0]) // 2

        #temporary board to check for collision for new piece
        temp_grid = copy.deepcopy(self.grid)

        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = self.color_pieces["EMPTY"]
        
        #if there is not collision, apply change to the piece
        if (not self._check_collison(rotated_piece, temp_grid, self.current_piece_start_row, new_start_col)):
            for row in range(len(rotated_piece)):
                for col in range(len(rotated_piece[row])):
                    if rotated_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][new_start_col + col] = self.current_piece_color
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
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = self.color_pieces["EMPTY"]
                    
        while ((self.current_piece_start_row + 1 <= (self.TETRIS_ROWS - len(self.current_piece))) and (not self._check_collison(self.current_piece, temp_grid, self.current_piece_start_row + 1, self.current_piece_start_col))):
            self.current_piece_start_row += 1
        
        for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = self.current_piece_color
        
        self.grid = temp_grid
        self.last_move = "down"
        # self.tetris_testing_matrix()
        self.checkMatch()

    def _move_left(self):
        '''
        Move the piece to the left by one column when "a" is pressed
        '''
        temp_grid = copy.deepcopy(self.grid)

        for row in range(len(self.current_piece)):
            for col in range(len(self.current_piece[row])):
                if self.current_piece[row][col] == 1:
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = self.color_pieces["EMPTY"]
                    
        if (((self.current_piece_start_col - 1) >= 0) and (not self._check_collison(self.current_piece, temp_grid, self.current_piece_start_row, self.current_piece_start_col - 1))): #??
            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col - 1 + col] = self.current_piece_color
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
                    temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + col] = self.color_pieces["EMPTY"]
        
        if ((self.current_piece_start_col + 1 <= (self.TETRIS_COLS - len(self.current_piece[0]))) and not self._check_collison(self.current_piece, temp_grid, self.current_piece_start_row, self.current_piece_start_col + 1)): #??
            for row in range(len(self.current_piece)):
                for col in range(len(self.current_piece[row])):
                    if self.current_piece[row][col] == 1:
                        temp_grid.matrix[self.current_piece_start_row + row][self.current_piece_start_col + 1 + col] = self.current_piece_color
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
                if (grid.return_grid()[start_row + row][start_col + col].getPieceType() != Color.BLACK and new_piece[row][col] == 1):
                    return True
        return False
    
    def _check_score_complete(self) -> bool:
        '''
        Check if the current player has reached a certain score
        '''
        return self.players[self.current_player_index].getScore() >= self.END_GAME_SCORE
    
    def printGrid(self):
        for r in range(self.TETRIS_ROWS):
            new_row = []
            for c in range(self.TETRIS_COLS):
                new_row.append(self.grid.matrix[r][c].getPieceStr())
            print(new_row)

    def makeLower(self):
        '''
        Translates the Grid of GamePiece objects into the Color strings needed for tkinter. 
        '''
        str_matrix = []

        for row in range(self.TETRIS_ROWS):
            row_matrix =  []
            for column in range(self.TETRIS_COLS):
                row_matrix.append(self.grid.matrix[row][column].getPieceStr())
            str_matrix.append(row_matrix)

        return str_matrix
    
    # def tetris_testing_matrix(self):
    #     for row in range(self.TETRIS_ROWS):
    #         for col in range(self.TETRIS_COLS):
    #             print(("| " + self.grid.matrix[row][col].getPieceStr() + " |").center(15), end="")
    #         print("\n ____________________________________________________________________________")
    #     print("\n")
    #     print("\n")
    
    def runGame(self):
        self.printInstructions()
        self.populateInitialGrid()
        self.gui = TetrisGridGUI(self.makeLower(), self)
        self.gui.run()
        
# if __name__ == "__main__":
#     players = [Player('p1'), Player('p2')]
#     tet = Tetris(players)
#     tet.runGame()