from Grid import Grid
from game import Game
from Color import Color
import random

from collections import namedtuple
Coordinate = namedtuple('Coordinate', ['x', 'y'])

class Bejeweled(Game) :
    GAME_NAME = 'Bejeweled'
    BEJEWELED_ROWS = 8
    BEJEWELED_COLS = 8

    def __init__(self, players):
        super.__init__(self, self.BEJEWELED_ROWS, self.BEJEWELED_COLS, self.GAME_NAME, players)
        self._match_coordinates = []
        # create board for game here ~ clear any matches beforehand until no more ?
        # have a preset board? "Levels"


    def populate_initial_grid(self):
        colors = list(Color)
        for i in range(self.BEJEWELED_ROWS):
            for j in range(self.BEJEWELED_COLS):
                self.grid[i][j] = random.choice(colors)
        self.checkGridMatch() # clear board of matches
    
    def addNewPieces(self):
        # checks every grid square, if the grid square is empty, fill it with a new piece
        pass

    def processUserInput(self, user_input):
        pass    
    
    def endGame(self) -> bool:
        pass

    def checkMatch(self):
        pass

    def _checkGridMatch(self) -> int:
        pass
            
    def _checkMoveMatch(self) -> int:
        pass

    def _removeMatch(self):
        '''
        Removes valid matches from the Grid based on the coordinates found in 
        '''
        for coord in self._match_coordinates:
            self.grid[coord.x][coord.y] = Color.COLORLESS

    def _checkRowMatch(self):
        '''
        Checks for valid row matches, and clears any matches that are detected, moving
        any surrounding pieces down if necessary.
        '''
        for i in range(self.BEJEWELED_ROWS):
            for j in range(self.BEJEWELED_COLS-2):
                self._match_coordinates = [Coordinate(i, j)]
                if self._rowMatchLength(self, i, j) >= 3:
                    self._removeMatch()
                    # move pieces above down/add new pieces
                    # update score
                    pass


    def _checkColMatch(self):
        '''
        Checks for valid column matches, and clears any matches that are detected, moving
        any surrounding pieces down if necessary.
        '''
        for i in range(self.BEJEWELED_ROWS-2):
            for j in range(self.BEJEWELED_COLS):
                if self._colMatchLength(self, i, j) >= 3:
                    # remove match
                    # move pieces above down/add new pieces
                    # update score
                    pass


    def _rowMatchLength(self, x, y) -> int:
        '''
        Returns the length of the horizontal "Match" made from the current coordinate in the Grid.
        If the value returned is 3+, there is a vertical match.
        '''
        gem_color = self.grid[x][y]
        match_length = 1
        col_position = y
        
        # Checking gem to the right
        while self.checkForSameColors(gem_color, x, col_position+1): 
            self._match_coordinates.append(Coordinate(x, col_position+1))
            match_length += 1
            col_position += 1
        
        # Setting column position back to the source gem
        col_position = y
        
        # Checking gem to the left
        while self.checkForSameColors(gem_color, x, col_position-1): 
            self._match_coordinates.append(Coordinate(x, col_position-1))
            match_length += 1
            col_position -= 1

        # Returns the length of the match (not a true match if match_length < 3)
        return match_length


    def _colMatchLength(self, x, y) -> int:
        '''
        Returns the length of the vertical "Match" made from the current coordinate in the Grid.
        If the value returned is 3+, there is a vertical match.
        '''
        gem_color = self.grid[x][y]
        match_length = 1
        row_position = x

        # Checking above the gem
        while (self.checkForSameColors(gem_color, row_position-1, y)):
            self._match_coordinates.append(Coordinate(row_position-1, y))
            row_position -= 1
            match_length += 1
        
        # Setting row_position back to the source gem
        row_position = x

        # Checking below the gem
        while (self.checkForSameColors(gem_color, row_position+1, y)):
            self._match_coordinates.append(Coordinate(row_position+1, y))
            row_position += 1
            match_length += 1
            
        # Returns the length of the match (not a true match if match_length < 3)
        return match_length


    def _checkForSameColors(self, gem_color, x, y) -> bool:
        '''
        Checks if the adjacent gems are the same type [x and y are the coordinates of the adjacent gem].
        Returns False if the coordinates are out of bounds or if the gem colors do not match.
        Returns True if the gem colors do match!
        '''
        # error bounds
        if x < 0 or x >= self.BEJEWELED_ROWS:
            return False
        if y < 0 or y >= self.BEJEWELED_COLS:
            return False

        return gem_color == self.grid[x][y]

        
    def _movePiecesDown(self):
        '''
        Given the match coordinates, moves the pieces down in each column
        '''
        for coord in self._match_coordinates:
            row = coord.x
            col = coord.y
            for r in range(row, 0, -1): # Move everything down in a singular column
                # Move the piece down by one position
                self.grid[r][col] = self.grid[r - 1][col]
            # Set the topmost piece in the column to None
            self.grid[0][col] = None
