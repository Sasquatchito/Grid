from src.Cell import cell;
import queue
import random 

'''
Created by Hector Cervantes
Date: 07/07/2020

This class will be used to represent a "grid" of many different shapes and sizes.
'''
class grid:
    def __init__(self, cell):
        self.root = cell 
        self.north = cell
        self.south = cell
        self.west = cell 
        self.east = cell
        self.cell_num = 0
        self.x = 0
        self.y = 0
    
    def set_root(self, cell):
        self.cell = cell

    def get_root(self):
        return self.root


    def build_grid(self, x, y):
        self.build_rows(x, y)
        self.connect_cells()
    
    def build_rows(self, x, y):
        self.x = x
        self.y = y
        temp = self.root
        for i in range(0, x):
            temp2 = temp 
            for j in range(1, y):
                self.add_east_cell(temp2, 0)
                temp2 = temp2.get_east()
            if(i + 1 != x):
                self.add_south_cell(temp, 0)
                temp = temp.get_south()
    
    def connect_cells(self):
        row = self.root
        next_row = self.root.south;
        while(next_row.south is not None):
            temp1 = row
            temp2 = next_row
            while(temp1 is not None):
                temp1.set_south(temp2)
                temp2.set_north(temp1)
                temp1 = temp1.get_east()
                temp2 = temp2.get_east()
            row = next_row
            next_row = next_row.get_south()

    def add_east_cell(self, c, val = 0):
        e_cell = cell(val)
        e_cell.set_west(c)
        c.set_east(e_cell)
        self.increment_cell_numer()
        c.east.set_id(self.cell_num)

    def add_west_cell(self, c, val = 0):
        w_cell = cell(val)
        w_cell.set_east(c)
        c.set_west(w_cell)
        self.increment_cell_numer()
        c.east.set_id(self.cell_num)
    
    def add_south_cell(self, c, val = 0):
        s_cell = cell(val)
        s_cell.set_north(c)
        c.set_south(s_cell)
        self.increment_cell_numer()
        c.east.set_id(self.cell_num)
    
    def add_north_cell(self, c, val = 0):
        n_cell = cell(val)
        n_cell.set_south(c)
        c.set_north(n_cell)
        self.increment_cell_numer()
        c.east.set_id(self.cell_num)
    
    def increment_cell_numer(self):
        self.cell_num += 1
    
    def get_cell(self, id):
        print("Finding Cell")

    def print_grid(self):
        temp = self.root
        while(temp is not None):
            temp2 = temp
            while(temp2 is not None):
                print(str(temp2.get_val()), end='')
                temp2 = temp2.get_east()
            print()
            temp = temp.get_south()
