import tkinter as tk
from GridGUI import GridGUI

class TetrisGridGUI(GridGUI):
    GRID_WIDTH = 300
    GRID_HEIGHT = 600
    LINE_WIDTH = .5
    
    def __init__(self, matrix, tetris_obj):
        self.window = None
        self.canvas = None
        self.matrix = matrix
        self.tetris_obj = tetris_obj
        self.cols = tetris_obj.TETRIS_COLS
        self.rows = tetris_obj.TETRIS_ROWS
        self.block_w = self.GRID_WIDTH/self.cols
        self.block_h = self.GRID_HEIGHT/self.rows
        
    def onKeyPress(self, event):
        key = event.keysym
        self.tetris_obj.processUserInput(key)
                
        self.matrix = self.tetris_obj.makeLower()
        self.fill_canvas(self.matrix, self.canvas, self.block_w, self.block_h)
        
    def run(self):
        self.window = tk.Tk()
        # Draw Grid
        self.canvas = self.draw_grid(self.window, self.GRID_WIDTH, self.GRID_HEIGHT, self.cols, self.rows, self.LINE_WIDTH)
        
        #When w, a, s, or d is pressed
        self.window.bind('<KeyPress>', lambda e : self.onKeyPress(e))
        
        self.fill_canvas(self.matrix, self.canvas, self.block_w, self.block_h)
        
        self.window.mainloop()

        
        
                
            
            
    
    