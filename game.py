# game.py
from abc import ABC, abstractmethod 
from Grid import Grid

class Game(ABC):
    '''
    This is the abstract class from which all Tile Matching Games inherit from.
    We included template methods that standardize the generic game loop, while allowing
    for each TMG to implement their own varying game logic. 
    '''

    # No init b/c nothing should be instantiated as an abstract Game object
    # def __init__(self, num_rows, num_cols, game_name, players) -> None:
    #     self.grid_rows = num_rows
    #     self.grid_cols = num_cols
    #     self.game_name = game_name
    #     self.grid = Grid(self.grid_rows, self.grid_cols)
    #     self.players = players
    #     self.current_player_index = 0 # so you know who to give points to?
        

    def runGameLoop(self):
        '''
        This is the template method for all TMGs. It outlines the general game loop
        that each TMG should follow.
        '''
        self.populate_initial_grid()
        while(not self.endGame()):
            # self.addNewPieces() ~ prob better to call when processing game matches.
            user_input = self.takeUserInput()
            self.processUserInput(user_input)
            self.checkMatch() # update score if necessary inside this method
            # update display ~ updated within various functions too?
    
    
    @abstractmethod       
    def populate_initial_grid(self):
        pass
    
    @abstractmethod
    def addNewPieces(self):
        pass
    
    def takeUserInput(self):
        user_input = input()
        return user_input

    @abstractmethod    
    def processUserInput(self, user_input):
        pass    
    
    @abstractmethod
    def endGame(self) -> bool:
        pass

    @abstractmethod
    def checkMatch(self):
        pass

    

    