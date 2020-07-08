from .Cell import Cell;
import queue

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
        self.cell_num = 0;
    
    def set_root(self, cell):
        self.cell = cell

    def get_root(self,cell):
        return self.cell

    def add_east_cell(self, cell, val = 0):
        cell.set_east_cell(cell(0))
        self.increment_cell_numer()
        cell.east.set_id(self.cell_num)

    def build_grid(self, x, y):
        self.build_rows(x, y)
        self.connect_cells()
    
    def build_rows(self, x, y):
        temp = self.root
        for i in range(0, x):
            temp2 = temp 
            for j in range(0, y):
                temp2.set_east_cell(cell(0))
                temp2 = temp2.get_east()
            temp.set_south_cell(cell(0))
            temp = temp.get_south()
    
    def connect_cells(self):
        row = self.root
        next_row = self.root.south;
        while(next_row.south is not None):
            temp1 = row
            temp2 = next_row
            while(temp1 is not None):
                temp1.set_south_cell(temp2)
                temp2.set_north_cell(temp1)
                temp1 = temp1.get_east()
                temp2 = temp2.get_east()
            row = row.get_south()
            next_row = next_row.get_south()

    def add_west_cell(self, cell, val = 0):
        cell.set_west_cell(cell(0))
        self.increment_cell_numer()
        cell.east.set_id(self.cell_num)
    
    def add_south_cell(self, cell, val = 0):
        cell.set_south_cell(cell(0))
        self.increment_cell_numer()
        cell.east.set_id(self.cell_num)
    
    def add_north_cell(self, cell, val = 0):
        cell.set_north_cell(cell(0))
        self.increment_cell_numer()
        cell.east.set_id(self.cell_num)
    
    def increment_cell_numer(self):
        self.cell_num += 1
    
    def get_cell(self, id):
        print("Finding Cell")

    def print_grid(self):
        temp = self.root
        while(temp is not None):
            temp2 = temp
            while(temp2 is not None):
                print(temp.get_val(), end='')
                temp2 = temp2.get_east()
            print()
            temp = temp.get_south()
