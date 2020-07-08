from src.Cell import cell 
from src.Grid import grid
from src.Maze import maze

def start():
    c = cell(0)
    g = grid(c)
    x = 10
    y = 10
    g.build_grid(x, y)
    root = g.get_root()
    root.set_val(1)
    root.get_east().set_val(2)
    
    print("Here is a " + str(x) + " by " + str(y) + " grid.")
    g.print_grid()

start()