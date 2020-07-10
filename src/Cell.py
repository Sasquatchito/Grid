'''
Created by Hector Cervantes
Date: 07-07-2020

This class represents a "cell" in a grid that will be used as building blocks for Grid Objects.
'''

class cell:
    def __init__(self, val=0, x=0, y=0, east=None, west=None, north=None, south=None):
        self.east = east
        self.west = west
        self.north = north
        self.south = south
        self.edge_cell = False
        self.val = val
        self.x = 0
        self.y = 0
        self.id = 0

    def set_x(self, x):
        self.x = x
    
    def set_y(self, y):
        self.y = y

    def set_val(self, val):
        self.val = val

    def set_south(self, south):
            self.south = south
    
    def set_north(self, north):
           self.north = north
            
    def set_east(self, east):
            self.east = east
    
    def set_west(self, west):
            self.west = west
    
    def get_id(self):
        return self.id

    def get_val(self):
        return self.val

    def get_south(self):
        return self.south
    
    def get_north(self):
        return self.north
    
    def get_east(self):
        return self.east
    
    def get_west(self):
        return self.west
    
    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def is_corner_cell(self):
        ne_corner = self.east is None and self.north is None
        se_corner = self.east is None and self.south is None
        sw_corner = self.west is None and self.north is None 
        nw_corner = self.west is None and self.south is None 
        return ne_corner or se_corner or sw_corner or nw_corner
    
    def is_peninsula_cell(self):
        sum = (self.east == None) + (self.north == None) + (self.south == None) + (self.west == None)
        return  sum == 3
    
    def is_isalnd_cell(self):
        sum = (self.east == None) + (self.north == None) + (self.south == None) + (self.west == None)
        return  sum == 4

    def is_mainland_cell(self):
        sum = (self.east != None) + (self.north != None) + (self.south != None) + (self.west != None)
        return  sum == 4