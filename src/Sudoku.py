
from src.Cell import cell
from src.Grid import grid


class sudoku():
    def __init__(self):
        grids = []
        for x in range(9):
            grids.append(grid(cell(0)))
        self.build_sudoku_grids()
    
    def build_sudoku_grids(self):
       for x in self.grids:
           x.buld_grid(3,3);
       