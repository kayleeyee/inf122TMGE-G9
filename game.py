# game.py
from abc import ABC, abstractmethod 
from Grid import Grid

class Game(ABC):
    '''
    This is the abstract class from which all Tile Matching Games inherit from.
    We included template methods that standardize the generic game loop, while allowing
    for each TMG to implement their own varying game logic. 
    '''        

    
    @abstractmethod
    def runGame(self):
        pass
    
    @abstractmethod
    def printInstructions(self):
        pass

    @abstractmethod
    def displayPlayerScore(self):
        pass
    
    @abstractmethod       
    def populateInitialGrid(self):
        pass
    
    @abstractmethod
    def addNewPieces(self):
        pass

    @abstractmethod    
    def processUserInput(self, user_input):
        pass    
    
    @abstractmethod
    def endGame(self):
        pass

    @abstractmethod
    def checkMatch(self):
        pass

    
    

    