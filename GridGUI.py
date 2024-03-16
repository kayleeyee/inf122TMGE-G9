import tkinter as tk
from abc import ABC, abstractmethod 
 

class GridGUI(ABC):
    '''
    Abstract GUI class that Game objects use to develop their GUIs
    '''
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


    @abstractmethod
    def run(self):
        pass