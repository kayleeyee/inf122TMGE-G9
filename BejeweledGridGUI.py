# BejeweledGridGUI.py
# by Kaylee and Kele
import tkinter as tk
from GridGUI import GridGUI

class BejeweledGridGUI(GridGUI.GridGUI):
    WINDOW = None
    CANVAS = None
    COLS = 0
    ROWS = 0
    GRID_WIDTH = 500
    GRID_HEIGHT = 500
    BLOCK_W = 0
    BLOCK_H = 0
    LINE_WIDTH = .5
    MATRIX_ARR = []

    def __init__(self):
        pass
    
    def detectClick(self, x: int, y: int, b_width, b_height, game_object):
        i, j = self.canvas_to_matrix(x, y, b_width, b_height)
        game_object.processUserInput(j, i)
        self.MATRIX_ARR = game_object.makeLower(game_object.grid.matrix)
        
        self.fill_canvas(self.MATRIX_ARR, self.CANVAS, self.BLOCK_W, self.BLOCK_H)

        #DEBUG:
        print("Coordinate:",j, i)

    # def onKeyPress(self, event):
    #     if event.keysym == 's':
    #         print("'s' key pressed")
    #

    def run(self, num_rows, num_cols, matrix, game_object):
        self.WINDOW = tk.Tk()

        self.GRID_WIDTH = 500
        self.GRID_HEIGHT = 500
                   
        self.COLS = num_cols
        self.ROWS = num_rows

        # Leave these for clarity
        self.BLOCK_W = self.GRID_WIDTH/self.COLS
        self.BLOCK_H = self.GRID_HEIGHT/self.ROWS
        self.LINE_WIDTH = .5
        self.CANVAS = self.draw_grid(self.WINDOW, self.GRID_WIDTH, self.GRID_HEIGHT, self.COLS, self.ROWS, self.LINE_WIDTH) # Draw Grid

        # When Left Mouse Button is clicked
        self.WINDOW.bind('<Button-1>', lambda e : self.detectClick(e.x, e.y, self.BLOCK_W, self.BLOCK_H, game_object)) # Handle Events

        # When "s" is pressed (Shuffle the board)
        # self.WINDOW.bind('<KeyPress>', lambda e : self.onKeyPress(e))

        self.MATRIX_ARR = matrix
        self.fill_canvas(self.MATRIX_ARR, self.CANVAS, self.BLOCK_W, self.BLOCK_H)

        self.WINDOW.mainloop()
        # If the game returns end game is true, then I have to stop the main loop
        # TODO: Look for how to end this


