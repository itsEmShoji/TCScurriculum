class Coordinate:

    def __init__(self, row_in, col_in, lev_in, val_in):
        # TODO: initialize all of our instance variables
        # (row, col, level, value, stepped, prev)

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    def print_coord(self):
        # TODO: print 'coord:(level, row, coord)'

    def is_walkable(self):
        # TODO: A coordinate is walkable if it is not a trap or wall and it has not been stepped on previously

    def get_neighbor(self, dir, temple_map):
        if dir == 'n':
            return temple_map[self.level][self.row-1][self.col]
        elif dir == 'e':
            return temple_map[self.level][self.row][self.col+1]
        elif dir == 's':
            return temple_map[self.level][self.row+1][self.col]
        elif dir == 'w':
            return temple_map[self.level][self.row][self.col-1]
        elif dir == 'u':
            return temple_map[self.level+1][self.row][self.col]
        elif dir == 'd':
            return temple_map[self.level-1][self.row][self.col]

    def step(self):
        # TODO: if we have already stepped on this coordinate, print "STEPPING TWICE"
        # TODO: set stepped equal to True
