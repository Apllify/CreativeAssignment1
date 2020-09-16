import math


#setting up grid dimensions
grid_width = 4
grid_height = 4


#setting up grid itself
grid = ["▯"] * grid_width * grid_height



#change the width of the display grid, RESETS THE CURRENT GRID
def set_grid_width(new_grid_width):
    
    global grid_width
    global grid
    
    grid_width = new_grid_width
    grid = ["▯"] * grid_width * grid_height
    


#change the height of the display grid, RESETS THE CURRENT GRID
def set_grid_height(new_grid_height):
    
    global grid_height
    global grid
    
    grid_height = new_grid_height
    grid = ["▯"] * grid_width * grid_height
    

#RESETS THE CURRENT GRID
def reset_grid():
    global grid 
    
    grid = ["▯"] * grid_width * grid_height
    
    
    
#Set the grid element at coordinates (x, y) to value // X AND Y BOTH START AT 0 // (0, 0) IS THE TOP LEFT OF THE GRID
def set_grid_element_at(x, y, value):
    
    global grid
    
    if x not in range(0, grid_width) or y not in range(0, grid_height):
        raise Exception("Coordinates are not valid")
        
    if not isinstance(value, str):
        raise Exception("Value must be string")
        
    if len(value) != 1:
        raise Exception("Value must be string of length 1 (one)")
        
    grid[x * grid_width + y] = value
    
    
    
#display the output grid
def display():            
    for i in range(grid_width):
        for j in range(grid_height):
            print(grid[i * grid_width + j], end = " ")
            
        print()
        
        
    
    

    
    
    
    