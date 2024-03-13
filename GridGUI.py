import tkinter as tk

# Grid GUI
class GridGUI:
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

    # def __init__(self):
    #     pass
    
    def draw_grid(self, window : tk.Tk, width, height, num_col, num_row, line_width) -> tk.Canvas:
        window.geometry = str(width)+"x"+str(height)
        canvas = tk.Canvas(window, width=width, height=height)
        
        # Draw column lines
        x0 = width/num_col
        for _ in range(num_col-1):
            canvas.create_line(x0, 0, x0, height, fill="black", width=line_width)
            x0 += width/num_col
    
        # Draw row lines
        y0 = height/num_row
        for _ in range(num_row-1):
            canvas.create_line(0, y0, width, y0, fill = "black", width=line_width)
            y0 += height/num_row # Get ready for next row
            
        canvas.pack()
        return canvas

    # Returns the actual coordinates (x, y) for the canvas
    # given the location in the matrix
    def matrix_to_canvas(self, i : int, j: int, b_width, b_height) -> tuple:
        return (i*b_width, j*b_height)

    # Returns the matrix coordinates
    # given the location in the canvas
    # B_width refers to the width of 
    # some grid on the screen
    def canvas_to_matrix(self, x: int, y: int, b_width, b_height) -> tuple:
        return (int(x//b_width), int(y//b_height))
            
    # This will pass the input to the 
    # specific game instance 
    def pass_input(self, x: int, y: int, b_width, b_height, game_object):
        # Will eventually call something
        # diff than print
        i, j = self.canvas_to_matrix(x, y, b_width, b_height)
        game_object.processUserInput(j, i)
        self.MATRIX_ARR = game_object.makeLower(game_object.grid.matrix)
        
        self.fill_canvas(self.MATRIX_ARR, self.CANVAS, self.BLOCK_W, self.BLOCK_H)
        print("Coordinate:",j, i)


    # Take in a matrix and display each square
    # Let's suppose it's a list of colors for now
    # This can change in the future
    def fill_canvas(self, arr : list, canvas : tk.Canvas, b_width, b_height) -> None:
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                y, x = self.matrix_to_canvas(i, j, b_width, b_height)
                color = arr[i][j]
                # In the case of tetris, this outline might change so that they layer
                canvas.create_rectangle(x,y,x+b_width,y+b_height, fill=color, outline = "black")    


    def run(self, num_rows, num_cols, matrix, game_object):
        self.WINDOW = tk.Tk()
        # These constants can be replaced with your grid 
        # also input a set amount that works with Bejeweled/Tetris
        self.GRID_WIDTH = 500
        self.GRID_HEIGHT = 500
                   
        self.COLS = num_cols
        self.ROWS = num_rows

        # Leave these for clarity
        self.BLOCK_W = self.GRID_WIDTH/self.COLS
        self.BLOCK_H = self.GRID_HEIGHT/self.ROWS
        self.LINE_WIDTH = .5
        self.CANVAS = self.draw_grid(self.WINDOW, self.GRID_WIDTH, self.GRID_HEIGHT, self.COLS, self.ROWS, self.LINE_WIDTH) # Draw Grid
        self.WINDOW.bind('<Button-1>', lambda e : self.pass_input(e.x, e.y, self.BLOCK_W, self.BLOCK_H, game_object)) # Handle Events

        self.MATRIX_ARR = matrix
        self.fill_canvas(self.MATRIX_ARR, self.CANVAS, self.BLOCK_W, self.BLOCK_H)

        self.WINDOW.mainloop()
        # If the game returns end game is true, then I have to stop the main loop
        # TODO: Look for how to end this

    # Call run(), in order to run this
    # run()
