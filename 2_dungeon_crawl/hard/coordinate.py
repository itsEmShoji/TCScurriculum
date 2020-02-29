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
        # TODO: if dir is north, return temple map one row down
        # TODO: else if dir is east, return temple_map one column up
        # TODO: else if dir is south, return temple_map one row up
        # TODO: else if dir is west, return temple_map one column down
        # TODO: else if dir is up, return temple_map one level up
        # TODO: else if dir is down, return temple_map one level down

    def step(self):
        # TODO: if we have already stepped on this coordinate, print "STEPPING TWICE"
        # TODO: set stepped equal to True
