from Grid import Grid
from game import Game
from Color import Color
from player import Player
from BejeweledGridGUI import BejeweledGridGUI
import random

from collections import namedtuple
Coordinate = namedtuple('Coordinate', ['x', 'y'])

class Bejeweled(Game) :
    GAME_NAME = 'Bejeweled'
    BEJEWELED_ROWS = 8
    BEJEWELED_COLS = 8
    BEJEWELED_COLORS = 7
    BEJEWELED_3_MATCH = 10
    BEJEWELED_4_MATCH = 20
    BEJEWELED_5_MATCH = 30
    BEJEWELED_LEVEL_1 = 50

    def __init__(self, players):
        self.grid = Grid(self.BEJEWELED_ROWS, self.BEJEWELED_COLS)
        self.players = players
        self._current_player_index = 0
        self._match_coordinates = []
        self._colors = list(Color)[:self.BEJEWELED_COLORS] 
        self._clicked_gems_coordinates = []


    def printInstructions(self):
        '''
        Prints instructions on how to play Bejeweled to the player's terminal
        '''
        instructions = 'Welcome to Bejeweled!\nTo play this game, click on any two adjacent gems to make a 3-5 gem match!\nIf you need to shuffle the board, press "s"'
        print(instructions)
    
    
    def displayPlayerScore(self):
        print(f"{self.players[self._current_player_index].getName()}'s score: {self.players[self._current_player_index].getScore()}")


    def populateInitialGrid(self):
        '''
        Bejeweled's grid initialization. Method fills the Grid with random Color values, then
        checks for any matches that may have been made in the Grid initialization, clearing them
        until there are no more matches left on the board.
        '''
        for i in range(self.BEJEWELED_ROWS):
            for j in range(self.BEJEWELED_COLS):
                self.grid.matrix[i][j] = random.choice(self._colors)
        self._checkGridMatch() # clear board of matches, don't care about the score generated


    def addNewPieces(self):
        # checks every grid square, if the grid square is empty, fill it with a new piece
        for i in range(self.BEJEWELED_ROWS):
            for j in range(self.BEJEWELED_COLS):
                if self.grid.matrix[i][j] == Color.COLORLESS:
                    self.grid.matrix[i][j] = random.choice(self._colors)

        # add score to current player!
        score = self._checkGridMatch() 
        return score


    def processUserInput(self, j, i):
        if Coordinate(j, i) not in self._clicked_gems_coordinates and len(self._clicked_gems_coordinates) < 2:
            self._clicked_gems_coordinates.append(Coordinate(j, i))
        
        if len(self._clicked_gems_coordinates) == 2:
            old_x = self._clicked_gems_coordinates[0].x
            old_y = self._clicked_gems_coordinates[0].y
            new_x = self._clicked_gems_coordinates[1].x
            new_y = self._clicked_gems_coordinates[1].y
            self._swapGems(old_x, old_y, new_x, new_y)
            self.checkMatch()
            self.displayPlayerScore()
            self.endGame()
                

    def endGame(self) -> bool:
        '''
        Indicates whether the game is over or not.
        '''
        if self._current_player_index == len(self.players):
            # print winner/scores
            exit()

        if self._level_complete():
            # end game for current player
            print(f'\nGAME OVER for {self.players[self._current_player_index].getName()}\n')
            self._current_player_index += 1

            # if there are players left, start their game
            if self._current_player_index < len(self.players):
                print(f'\nSTART GAME for {self.players[self._current_player_index].getName()}\n')
                self.populateInitialGrid()

            return True

        return False


    def checkMatch(self):
        '''
        If two gems have been switched, this method checks to see if any matches were made.
        From there, the player's score if updated
        '''
        if len(self._clicked_gems_coordinates) == 2:
            # if the swap was invalid, this variable is len 0 again
            old_x = self._clicked_gems_coordinates[0].x
            old_y = self._clicked_gems_coordinates[0].y
            new_x = self._clicked_gems_coordinates[1].x
            new_y = self._clicked_gems_coordinates[1].y

            score = self._checkMoveMatch(new_x, new_y, old_x, old_y)

            # update player score
            self.players[self._current_player_index].addToScore(score)

            # empty clicked gems
            self._clicked_gems_coordinates = []


    def _level_complete(self) -> bool:
        '''
        Ends Bejeweled game for the Player if they achieved/passed the level's score requirement.
        '''
        return self.players[self._current_player_index].score >= self.BEJEWELED_LEVEL_1


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
            if (gem2_x - 1) == gem1_x:
                return True
            # if gem2 is to the below of gem1
            elif (gem2_x + 1) == gem1_x:
                return True

        # all other cases: invalid swap
        return False

    def _swapGems(self, gem1_x, gem1_y, gem2_x, gem2_y):
        '''
        Swaps adjacent Gems within the Grid.
        '''
        if self._isValidSwap(gem1_x, gem1_y, gem2_x, gem2_y):
            self.grid.matrix[gem1_x][gem1_y], self.grid.matrix[gem2_x][gem2_y] = self.grid.matrix[gem2_x][gem2_y], self.grid.matrix[gem1_x][gem1_y]
        else:
            print("Invalid swap, try again.")
            self._clicked_gems_coordinates = []


    def _checkGridMatch(self) -> int:
        '''
        Checks whole board for any matches that were made (from falling/grid creation).
        If there were matches made, the score that the player's score should be increased by is returned.
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
                    current_score += self._checkRowMatch(row, col)

            # clearing column matches next 
            for row in range(self.BEJEWELED_ROWS-2):
                for col in range(self.BEJEWELED_COLS):
                    current_score += self._checkColMatch(row, col)
        
        return current_score
                
            
    def _checkMoveMatch(self, new_x, new_y, old_x, old_y) -> int:
        '''
        Checks surrounding area of a move made by the player to see if there was a match made.
        If a match was successful
        '''
        score = 0
        
        score += self._checkRowMatch(new_x, new_y)
        score += self._checkColMatch(new_x, new_y)
        score += self._checkRowMatch(old_x, old_y)
        score += self._checkColMatch(old_x, old_y)

        # if the move did not result in a match, swap back
        if score == 0:
            self._swapGems(new_x, new_y, old_x, old_y)
        
        # returns score, which should be added to player's total score
        return score


    def _removeMatch(self):
        '''
        Removes valid matches from the Grid based on the coordinates found in 
        '''
        for coord in self._match_coordinates:
            self.grid.matrix[coord.x][coord.y] = Color.COLORLESS


    def _checkRowMatch(self, x, y):
        '''
        Checks for valid row matches, and clears any matches that are detected, moving
        any surrounding pieces down if necessary.
        '''
        points_scored = 0
        self._match_coordinates = [Coordinate(x, y)]

        match_size = self._rowMatchLength(x, y)
        if match_size >= 3:
            # add points that the player should receive.
            if match_size == 3:
                points_scored += self.BEJEWELED_3_MATCH
            elif match_size == 4:
                points_scored += self.BEJEWELED_4_MATCH
            else:
                # only other possible match is a 5 match.
                points_scored += self.BEJEWELED_5_MATCH
            
            self._removeMatch()
            self._movePiecesDown()
            points_scored += self.addNewPieces()

        return points_scored


    def _checkColMatch(self, x, y):
        '''
        Checks for valid column matches, and clears any matches that are detected, moving
        any surrounding pieces down if necessary.
        '''
        points_scored = 0
        self._match_coordinates = [Coordinate(x, y)]

        match_size = self._colMatchLength(x, y)
        if match_size >= 3:
            # add points that the player should receive.
            if match_size == 3:
                points_scored += self.BEJEWELED_3_MATCH
            elif match_size == 4:
                points_scored += self.BEJEWELED_4_MATCH
            else:
                # only other possible match is a 5 match.
                points_scored += self.BEJEWELED_5_MATCH

            self._removeMatch()
            self._movePiecesDown()
            points_scored += self.addNewPieces()

        return points_scored


    def _rowMatchLength(self, x, y) -> int:
        '''
        Returns the length of the horizontal "Match" made from the current coordinate in the Grid.
        If the value returned is 3+, there is a vertical match.
        '''
        gem_color = self.grid.matrix[x][y]
        match_length = 1
        col_position = y
        
        # don't proceed if current cell is COLORLESS
        if gem_color == Color.COLORLESS:
            return match_length

        # Checking gem to the right
        while self._checkForSameColors(gem_color, x, col_position+1): 
            self._match_coordinates.append(Coordinate(x, col_position+1))
            match_length += 1
            col_position += 1
        
        # Setting column position back to the source gem
        col_position = y
        
        # Checking gem to the left
        while self._checkForSameColors(gem_color, x, col_position-1): 
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
        gem_color = self.grid.matrix[x][y]
        match_length = 1
        row_position = x

        # don't proceed if current cell is COLORLESS
        if gem_color == Color.COLORLESS:
            return match_length
        
        # Checking above the gem
        while (self._checkForSameColors(gem_color, row_position-1, y)):
            self._match_coordinates.append(Coordinate(row_position-1, y))
            row_position -= 1
            match_length += 1
        
        # Setting row_position back to the source gem
        row_position = x

        # Checking below the gem
        while (self._checkForSameColors(gem_color, row_position+1, y)):
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

        return gem_color == self.grid.matrix[x][y]

        
    def _movePiecesDown(self):
        '''
        Given the match coordinates, moves the pieces down in each column
        '''
        for coord in self._match_coordinates:
            row = coord.x
            col = coord.y
            for r in range(row, 0, -1): # Move everything down in a singular column
                # Move the piece down by one position
                self.grid.matrix[r][col] = self.grid.matrix[r - 1][col]
            # Set the topmost piece in the column to None
            self.grid.matrix[0][col] = Color.COLORLESS


    def printGrid(self):
        for r in range(self.BEJEWELED_ROWS):
            new_row = []
            for c in range(self.BEJEWELED_COLS):
                new_row.append(self.grid.matrix[r][c].name)
            print(new_row)

    def makeLower(self, matrix):
        new_matrix = []

        for row in range(self.BEJEWELED_ROWS):
            row_matrix =  []
            for column in range(self.BEJEWELED_COLS):
                # print(self.grid.matrix[row][column].name.lower())
                row_matrix.append(self.grid.matrix[row][column].name.lower())
            new_matrix.append(row_matrix)
        # print(new_matrix)
        return new_matrix


if __name__ == "__main__":
    players = [Player('p1'), Player('p2')]
    bj = Bejeweled(players)
    bj.populateInitialGrid()
    # bj.printGrid()
    gui = BejeweledGridGUI(bj.makeLower(bj.grid.matrix), bj)
    gui.run()
