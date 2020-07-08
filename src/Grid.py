class grid:
    def __init__(self, cell):
        self.root = cell 
        self.north = cell
        self.south = cell
        self.west = cell 
        self.east = cell
        self.cell_count = 0;
    
    def set_root(self, cell):
        self.cell = cell

    def get_root(self,cell):
        return self.cell
    
    def build_grid(self, cell_count):
        g = grid(self.root)
        q = queue.Queue()
        q.put(self.root)
        while(not q.empty()):
            cell = q.get()
            if(cell_count != 0):
                self.add_north_cell(cell, )
                self.add_south_cell()
                self.add_east_cell()
                self.add_west_cell()
                q.put(cell.get_north())
                q.put(cell.get_south())
                q.put(cell.get_west())
                q.put(cell.get_east())
            cell_count -= 1

    def add_east_cell(self, cell, val = 0):
        cell.set_east_cell(cell(0))
        cell.east.set(self.cell_count + 1)
    
    def add_west_cell(self, cell, val = 0):
        cell.set_west_cell(cell(0))
        cell.east.set(self.cell_count + 1)
    
    def add_south_cell(self, cell, val = 0):
        cell.set_south_cell(cell(0))
        cell.east.set(self.cell_count + 1)
    
    def add_north_cell(self, cell, val = 0):
        cell.set_north_cell(cell(0))
        cell.east.set(self.cell_count + 1)
    
    def get_cell(self, id):
        print("Finding Cell")

    def print_grid(self):
        print("Gonna print grid")