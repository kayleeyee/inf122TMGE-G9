import tkinter as tk

# Create Grid
def drawGrid(window : tk.Tk, width, height, num_col, num_row, line_width) -> None:
    window.geometry = str(width)+"x"+str(height)
    canvas = tk.Canvas(window, width=width, height=height)
    
     # Draw column lines
    x0 = width/num_col
    for _ in range(num_col-1):
        canvas.create_line(x0,0,x0,height, fill="black", width=line_width)
        x0 += width/num_col
   
    # Draw row lines
    y0 = height/num_row
    for _ in range(num_row-1):
        canvas.create_line(0, y0, width, y0, fill = "black", width=line_width)
        y0 += height/num_row # Get ready for next row

    canvas.pack()

# Returns the actual coordinates (x, y) for the canvas
# Given the location in the matrix
def findCoord(i : int, j: int):
    pass

# This will pass the input to the 
# specific game instance 
def passInput(x: int, y: int):
    # Will eventually call something
    # diff than print
    print(findCoord(x, y))


# Take in a matrix and display each square
# Not sure if we're gonna use actual images or not

def run():
    window = tk.Tk()

    GRID_WIDTH = 500;
    GRID_HEIGHT = 300;

    COL = 5;
    ROWS = 3;

    LINE_WIDTH = .5

    drawGrid(window, GRID_WIDTH, GRID_HEIGHT, COL, ROWS, LINE_WIDTH) # Draw Grid
    window.bind('<Button-1>', lambda e : passInput(e.x, e.y)) # Handle Events

    window.mainloop()

run()
