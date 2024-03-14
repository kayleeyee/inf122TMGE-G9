import tkinter as tk
from GridGUI import GridGUI

class BejeweledGridGUI(GridGUI):
    GRID_WIDTH = 500
    GRID_HEIGHT = 500
    LINE_WIDTH = .5

    def __init__(self, matrix, bejeweled_obj):
        self.window = None
        self.canvas = None
        self.matrix = matrix
        self.bejeweled_obj = bejeweled_obj
        self.cols = bejeweled_obj.BEJEWELED_COLS
        self.rows = bejeweled_obj.BEJEWELED_ROWS
        self.block_w = self.GRID_WIDTH/self.cols
        self.block_h = self.GRID_HEIGHT/self.rows
    

    def detectClick(self, x: int, y: int, b_width, b_height):
        i, j = self.canvas_to_matrix(x, y, b_width, b_height)

        self.bejeweled_obj.processUserInput(j, i)
        self.matrix = self.bejeweled_obj.makeLower(self.bejeweled_obj.grid.matrix)
        
        self.fill_canvas(self.matrix, self.canvas, self.block_w, self.block_h)

        #DEBUG:
        print("Coordinate:",j, i)


    def onKeyPress(self, event):
        if event.keysym == 's':
            print("'s' key pressed")
            self.bejeweled_obj.populateInitialGrid()
            self.matrix = self.bejeweled_obj.makeLower(self.bejeweled_obj.grid.matrix)
            self.fill_canvas(self.matrix, self.canvas, self.block_w, self.block_h)
    

    def run(self):
        self.window = tk.Tk()

        # Leave these for clarity

        self.canvas = self.draw_grid(self.window, self.GRID_WIDTH, self.GRID_HEIGHT, self.cols, self.rows, self.LINE_WIDTH) # Draw Grid

        # When Left Mouse Button is clicked
        self.window.bind('<Button-1>', lambda e : self.detectClick(e.x, e.y, self.block_w, self.block_h)) # Handle Events

        # When "s" is pressed (Shuffle the board)
        self.window.bind('<KeyPress>', lambda e : self.onKeyPress(e))

        self.fill_canvas(self.matrix, self.canvas, self.block_w, self.block_h)

        self.window.mainloop()
        # If the game returns end game is true, then I have to stop the main loop
        # TODO: Look for how to end this


