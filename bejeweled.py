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
    BEJEWELED_3_MATCH = 10
    BEJEWELED_4_MATCH = 20
    BEJEWELED_5_MATCH = 30
    BEJEWELED_LEVEL_1 = 500

    def __init__(self, players):
        super.__init__(self, self.BEJEWELED_ROWS, self.BEJEWELED_COLS, self.GAME_NAME, players)
        self._match_coordinates = []


    def populate_initial_grid(self):
        '''
        Bejeweled's grid initialization. Method fills the Grid with random Color values, then
        checks for any matches that may have been made in the Grid initialization, clearing them
        until there are no more matches left on the board.
        '''
        colors = list(Color)
        for i in range(self.BEJEWELED_ROWS):
            for j in range(self.BEJEWELED_COLS):
                self.grid[i][j] = random.choice(colors)
        self._checkGridMatch() # clear board of matches, don't care about the score generated


    def addNewPieces(self):
        # checks every grid square, if the grid square is empty, fill it with a new piece
        pass


    def processUserInput(self, user_input):
        pass    
    

    def endGame(self) -> bool:
        '''
        Indicates whether the game is over or not.
        '''
        if self._level_complete:
            return True

        return False


    def checkMatch(self):
        pass


    def _level_complete(self) -> bool:
        '''
        Ends Bejeweled game for the Player if they achieved/passed the level's score requirement.
        '''
        return self.players[self.current_player_index].score >= self.BEJEWELED_LEVEL_1


    def _isValidSwap(self, gem1_x, gem1_y, gem2_x, gem2_y):
        '''
        Checks to see if the gems are adjacent to each other.
        '''
        # when gems are in the same row
        if gem1_x == gem2_x:
            # if gem2 is to the left of gem1
            if (gem2_y - 1) == gem1_y:
                return True
            # if gem2 is to the right of gem1
            elif (gem2_y + 1) == gem1_y:
                return True
        
        # when gems are in the same column
        elif gem1_y == gem2_y:
            # if gem2 is to the above of gem1
            if (gem2_x - 1) == gem1_y:
                return True
            # if gem2 is to the below of gem1
            elif (gem2_x + 1) == gem1_y:
                return True

        # all other cases: invalid swap
        return False

    def _swapGems(self, gem1_x, gem1_y, gem2_x, gem2_y):
        '''
        Swaps Gems within the Grid.
        '''
        if self._isValidSwap(gem1_x, gem1_y, gem2_x, gem2_y):
            self._grid[gem1_x][gem1_y], self._grid[gem2_x][gem2_y] = self._grid[gem2_x][gem2_y], self._grid[gem1_x][gem1_y]


    def _checkGridMatch(self) -> int:
        '''
        Checks whole board for any matches that were made (from falling/grid creation).
        If there were matches made, the player's score is updated.
        '''
        old_score = -1
        current_score = 0

        # loop stops when score does not increase after an iteration
        # this means that no new gems were added to the board
        # OR that the new gems added to the board did not result in matches
        while (old_score != current_score):
            old_score = current_score
            # clearing row matches first
            for row in range(self.BEJEWELED_ROWS):
                for col in range(self.BEJEWELED_COLS-2):
                    score += self._checkRowMatch(row, col)

            # clearing column matches next 
            for row in range(self.BEJEWELED_ROWS-2):
                for col in range(self.BEJEWELED_COLS):
                    score += self._checkColMatch(row, col)
        
        #return current_score ?
                
            
    def _checkMoveMatch(self, new_x, new_y, old_x, old_y) -> int:
        '''
        Checks surrounding area of a move made by the player to see if there was a match made.
        If a match was successful
        '''
        # dunno if original swapping should also happen here?
        score = 0

        score += self._checkRowMatch(new_x, new_y)
        score += self._checkColMatch(new_x, new_y)

        # if the move did not result in a match, swap back
        if score == 0:
            self._swapGems(new_x, new_y, old_x, old_y)


    def _removeMatch(self):
        '''
        Removes valid matches from the Grid based on the coordinates found in 
        '''
        for coord in self._match_coordinates:
            self.grid[coord.x][coord.y] = Color.COLORLESS


    def _checkRowMatch(self, x, y):
        '''
        Checks for valid row matches, and clears any matches that are detected, moving
        any surrounding pieces down if necessary.
        '''
        self._match_coordinates = [Coordinate(x, y)]
        if self._rowMatchLength(self, x, y) >= 3:
            self._removeMatch()
            # move pieces above down/add new pieces
            # update score? or return score value?


    def _checkColMatch(self, x, y):
        '''
        Checks for valid column matches, and clears any matches that are detected, moving
        any surrounding pieces down if necessary.
        '''
        self._match_coordinates = [Coordinate(x, y)]
        if self._colMatchLength(self, x, y) >= 3:
            self._removeMatch()
            # move pieces above down/add new pieces
            # update score??


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
        kaylee
        '''
        pass
