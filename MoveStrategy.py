# MoveStrategy.py
from abc import ABC, abstractmethod
from player import Player 
from Grid import Grid

# ignore for now, probably don't need strategies for our design

class MoveStrategy(ABC):
    '''
    MoveStrategy is an interface for the moves that will be executed in TMGs
    '''
    @abstractmethod
    def executeMove(self, player : Player): # also takes the Grid?
        pass

class MoveRightStrategy(MoveStrategy):
    def executeMove(self, player : Player):
        pass
    
# MoveUp <- MoveUpRotate