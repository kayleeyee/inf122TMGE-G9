# game.py
from abc import ABC, abstractmethod 
from Grid import Grid

class Game(ABC):
    '''
    This is the abstract class from which all Tile Matching Games inherit from.
    We included template methods that standardize the generic game loop, while allowing
    for each TMG to implement their own varying game logic. 
    '''        

    def runGameLoop(self):
        '''
        This is the template method for all TMGs. It outlines the general game loop
        that each TMG should follow.
        '''
        self.populateInitialGrid()
        self.printInstructions()
        while(not self.endGame()):
            #user_input = self.takeUserInput()
            self.processUserInput()
            self.checkMatch() # update score if necessary inside this method
            self.displayPlayerScore()
            # update display ~ updated within various functions too?
    
    # TODO: Need to add a method that sends the grid to the GUI to update display
    # TODO: Add a method that displays which player is playing and the scores 
            # ^ feels like it can be done concretely, but players info is stored in concrete Game child classes :(
    
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
    
    # def takeUserInput(self):
    #     user_input = input()
    #     return user_input

    @abstractmethod    
    def processUserInput(self, user_input):
        pass    
    
    @abstractmethod
    def endGame(self) -> bool:
        pass

    @abstractmethod
    def checkMatch(self):
        pass


    
    

    