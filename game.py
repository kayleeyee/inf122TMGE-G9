# game.py
from abc import ABC, abstractmethod 
from Grid import Grid

class Game(ABC):
    '''
    This is the abstract class from which all Tile Matching Games inherit from.
    We included template methods that standardize the generic game loop, while allowing
    for each TMG to implement their own varying game logic. 
    '''

    game_name = ''
    grid = None
    players = []

    @abstractmethod
    def __init__(self, game_name, players) -> None:
        self.game_name = game_name
        self.players = players
        

    def runGameLoop(self):
        '''
        This is the template method for all TMGs. It outlines the general game loop
        that each TMG should follow.
        '''

        '''
        while(not endGame(self)):
            addNewPieces()
            takeUserInput()
            checkMatch()
        ''' 
    
    @abstractmethod
    def addNewPieces(self):
        pass
    
    @abstractmethod
    def takeUserInput(self):
        pass
        
    @abstractmethod
    def endGame(self) -> bool:
        pass

    @abstractmethod
    def checkMatch(self):
        pass

    