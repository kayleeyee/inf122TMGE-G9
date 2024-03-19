# MatchStrategy.py
from abc import ABC, abstractmethod
from player import Player 
from Grid import Grid
from GamePiece import GamePiece
from Color import Color

from collections import namedtuple
Coordinate = namedtuple('Coordinate', ['x', 'y'])

class MatchStrategy(ABC):
    '''
    MoveStrategy is an interface for the moves that will be executed in TMGs
    '''
    @abstractmethod
    def match(self, grid : Grid, coords : list[Coordinate]) -> list[Coordinate]:
        pass


class LocalHMatchStrategy(MatchStrategy):
    '''
    Checks for local horizontal matches within a Grid, and returns a list of Coordinates of the matches.
    '''
    def match(self, grid : Grid, coords : list[Coordinate]) -> list[Coordinate]:
        x = coords[0].x
        y = coords[0].y
        matches = [coords[0]]
        piece_type = grid.matrix[x][y].getPieceType()
        col_position = y
        
        # don't proceed if current cell is BLACK, no match made
        if piece_type == Color.BLACK:
            return []

        # Checking GamePiece to the right
        while self._checkForSamePieces(grid, piece_type, x, col_position+1): 
            matches.append(Coordinate(x, col_position+1))
            col_position += 1
        
        # Setting column position back to the source GamePiece
        col_position = y
        
        # Checking GamePiece to the left
        while self._checkForSamePieces(grid, piece_type, x, col_position-1): 
            matches.append(Coordinate(x, col_position-1))
            col_position -= 1

        # Returns the match Coordinates (not a true match if len(matches) < 3)
        if len(matches) < 3:
            matches = []

        return matches
    
    
    def _checkForSamePieces(self, grid : Grid, piece_type : GamePiece, x, y) -> bool:
        '''
        Checks if the adjacent GamePieces are the same type [x and y are the coordinates of the adjacent GamePiece].
        Returns False if the coordinates are out of bounds or if the GamePiece types do not match.
        Returns True if the GamePiece types do match!
        '''
        # error bounds
        if x < 0 or x >= grid.getRows():
            return False
        if y < 0 or y >= grid.getCols():
            return False

        return piece_type == grid.matrix[x][y].getPieceType()
    

class LocalVMatchStrategy(MatchStrategy):
    '''
    Checks for local vertical matches within a Grid, and returns a list of Coordinates of the matches.
    '''
    def match(self, grid : Grid, coords : list[Coordinate]) -> list[Coordinate]:
        x = coords[0].x
        y = coords[0].y
        matches = [coords[0]]
        piece_type = grid.matrix[x][y].getPieceType()
        row_position = x
        
        # don't proceed if current cell is BLACK, no match made
        if piece_type == Color.BLACK:
            return []

        # Checking above the GamePiece
        while self._checkForSamePieces(grid, piece_type, row_position+1, y): 
            matches.append(Coordinate(row_position+1, y))
            row_position += 1
        
        # Setting column position back to the source GamePiece
        row_position = x
        
        # Checking below the GamePiece
        while self._checkForSamePieces(grid, piece_type, row_position-1, y): 
            matches.append(Coordinate(row_position-1, y))
            row_position -= 1

        # Returns the match Coordinates (not a true match if len(matches) < 3)
        if len(matches) < 3:
            matches = []

        return matches

       
    def _checkForSamePieces(self, grid : Grid, piece_type : GamePiece, x, y) -> bool:
        '''
        Checks if the adjacent GamePieces are the same type [x and y are the coordinates of the adjacent GamePiece].
        Returns False if the coordinates are out of bounds or if the GamePiece types do not match.
        Returns True if the GamePiece types do match!
        '''
        # error bounds
        if x < 0 or x >= grid.getRows():
            return False
        if y < 0 or y >= grid.getCols():
            return False

        return piece_type == grid.matrix[x][y].getPieceType()
    
class HorizontalMatchStrategy(MatchStrategy):
    def match(self, grid : Grid, coords : list[Coordinate]) -> list[Coordinate]:
        start_x = coords[0].x
        end_x = coords[1].x
        end_y = coords[1].y
        
        rows_to_delete = []
        
        for row in range(start_x, end_x):
            row_all_color = True
            for col in range(end_y):
                if grid.return_grid()[row][col].getPieceType() == Color.BLACK:
                    row_all_color = False
                    break   
            if row_all_color:
                rows_to_delete.append(Coordinate(row, 0))
        return rows_to_delete