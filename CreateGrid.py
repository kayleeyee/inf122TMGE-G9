import tkinter as tk

# Create Grid
def draw_grid(window : tk.Tk, width, height, num_col, num_row, line_width) -> tk.Canvas:
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
    return canvas

# Returns the actual coordinates (x, y) for the canvas
# given the location in the matrix
def matrix_to_canvas(i : int, j: int, b_width, b_height) -> tuple:
    return (i*b_width, j*b_height)

# Returns the matrix coordinates
# given the location in the canvas
# B_width refers to the width of 
# some grid on the screen
def canvas_to_matrix(x: int, y: int, b_width, b_height) -> tuple:
    return (int(x//b_width), int(y//b_height))
        
# This will pass the input to the 
# specific game instance 
def pass_input(x: int, y: int, b_width, b_height):
    # Will eventually call something
    # diff than print
    i, j = canvas_to_matrix(x, y, b_width, b_height);
    print(j, i)


# Take in a matrix and display each square
# Let's suppose it's a list of colors for now
# This can change in the future
def fill_canvas(arr : list, canvas : tk.Canvas, b_width, b_height) -> None:
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            y, x = matrix_to_canvas(i, j, b_width, b_height)
            color = arr[i][j]
            # In the case of tetris, this outline might change so that they layer
            canvas.create_rectangle(x,y,x+b_width,y+b_height, fill=color, outline = "black")    

# Not sure if we're gonna use actual images or not

def run():
    window = tk.Tk()

    GRID_WIDTH = 500;
    GRID_HEIGHT = 300;

    COL = 5;
    ROWS = 3;

    BLOCK_W = GRID_WIDTH/COL
    BLOCK_H = GRID_HEIGHT/ROWS

    LINE_WIDTH = .5

    canvas = draw_grid(window, GRID_WIDTH, GRID_HEIGHT, COL, ROWS, LINE_WIDTH) # Draw Grid
    window.bind('<Button-1>', lambda e : pass_input(e.x, e.y, BLOCK_W, BLOCK_H)) # Handle Events

    matrix_arr = [["white","black","blue", "red", "purple"],
                  ["red","orange","white","yellow","white"],
                  ["orange","white","pink","purple","blue"]]
    
    fill_canvas(matrix_arr, canvas, BLOCK_W, BLOCK_H)

    window.mainloop()

run()
