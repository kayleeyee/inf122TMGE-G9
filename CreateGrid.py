import tkinter as tk

window = tk.Tk()

GRID_WIDTH = 500;
GRID_HEIGHT = 300;

COL = 5;
ROWS = 3;

LINE_WIDTH = .5

# Create Grid
def drawGrid():
    canvas = tk.Canvas(window, width=GRID_WIDTH, height=GRID_HEIGHT)
    
     # Draw column lines
    x0 = GRID_WIDTH/COL
    for _ in range(COL-1):
        canvas.create_line(x0,0,x0,GRID_HEIGHT, fill="black", width=LINE_WIDTH)
        print(x0)
        x0 += GRID_WIDTH/COL
   
    # Draw row lines
    y0 = GRID_HEIGHT/ROWS
    for _ in range(ROWS-1):
        canvas.create_line(0, y0, GRID_WIDTH, y0, fill = "black", width=LINE_WIDTH)
        y0 += GRID_HEIGHT/ROWS # Get ready for next row

    canvas.pack()

drawGrid()

# Returns the actual coordinates (x, y) for the canvas
# Given the location in the matrix
def findCoord(i : int, j: int):
    pass

window.mainloop()

# Take in a matrix and display each square
# Not sure if we're gonna use actual images or not
