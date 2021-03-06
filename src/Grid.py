from src.Cell import cell;
import queue
import random 

'''
Created by Hector Cervantes
Date: 07/07/2020

This class will be used to represent a "grid" of many different shapes and sizes.
'''
class grid():
    def __init__(self, cell):
        self.root = cell
        self.root.set_x(0)
        self.root.set_y(0)
        #grid corners 
        self.north = cell
        self.south = cell 
        self.east = cell 
        self.west = cell
        self.north_west = cell
        self.south_west = cell
        self.north_east = cell 
        self.south_east = cell
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
        e_cell = cell(val, c.get_x() ,c.get_y() + 1)
        e_cell.set_west(c)
        c.set_east(e_cell)
        self.increment_cell_numer()
        c.east.set_id(self.cell_num)
        if(c.get_east().get_y() > self.east.get_y()):
            self.east = c.get_east()

    def add_west_cell(self, c, val = 0):
        w_cell = cell(val, c.get_x() ,c.get_y() - 1)
        w_cell.set_east(c)
        c.set_west(w_cell)
        self.increment_cell_numer()
        c.east.set_id(self.cell_num)
        if(c.get_west().get_y() < self.west.get_y()):
            self.west = c.get_west()
    
    def add_south_cell(self, c, val = 0):
        s_cell = cell(val, c.get_x() - 1,c.get_y()) 
        s_cell.set_north(c)
        c.set_south(s_cell)
        self.increment_cell_numer()
        c.east.set_id(self.cell_num)
        if(c.get_south().get_x() < self.south.get_x()):
                self.south = c.get_south();
                if(self.south.get_y() <= self.west().get_y()):
                    self.south_west = c.get_south()
                elif(self.south.get_y() >= self.west().get_y()):
                    self.south_east = c.get_south()
    
    def add_north_cell(self, c, val = 0):
        n_cell = cell(val, c.get_x() + 1, c.get_y())
        n_cell.set_south(c)
        c.set_north(n_cell)
        self.increment_cell_numer()
        c.east.set_id(self.cell_num)
        if(c.get_north().get_x() > self.north.get_x()):
                self.north = c.get_north();
                if(self.north.get_y() <= self.west().get_y()):
                    self.north_west = c.get_north()
                elif(self.north.get_y() >= self.west().get_y()):
                    self.north_east = c.get_north()

    
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
