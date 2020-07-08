class cell:
    def __init__(self, val=0, east=None, west=None, north=None, south=None):
        self.east_neighbor = east
        self.west_neighbor = west
        self.north_neighbor = north
        self.south_neighbor = south
        self.edge_cell = False
        self.val = val
        self.id = 0
    
    def set_id(self, id):
        self.id = id

    def set_val(self, val):
        self.val = val

    def set_south(self, south):
        if(self.south is None):
            self.south = south
    
    def set_north(self, north):
        if(self.north is None):
           self.north = north
            
    def set_east(self, east):
        if(self.east is None):
            self.east = east
    
    def set_west(self, west):
        if(self.west is None):
            self.west = west
    
    def get_id(self):
        return self.id

    def get_val(self):
        return self.val

    def get_south(self):
        return self.south
    
    def set_north(self, north):
        return self.north
    
    def set_east(self, east):
        return self.east
    
    def set_west(self, west):
        return self.west
    
    def is_corner_cell(self):
        ne_corner = self.east == None and self.north == None
        se_corner = self.east == None and self.south == None
        sw_corner = self.west == None and self.north == None 
        nw_corner = self.west == None and self.south == None 
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