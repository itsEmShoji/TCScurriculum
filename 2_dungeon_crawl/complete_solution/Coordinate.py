class Coordinate:

    def __init__(self,row_in, col_in, lev_in, val_in):
        self.row = row_in
        self.col = col_in
        self.level = lev_in
        self.value = val_in
        self.stepped = False
        self.prev = None

    def __str__(self):
        return self.value

    def __repr__(self):
        return str(self)

    def print_coord(self):
        print(f"coord: ({self.level},{self.row},{self.col})")

    def is_walkable(self):
        return self.value != 't' and self.value != '|' and not self.stepped

    def get_neighbor(self, dir ,temple_map):
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
        if self.stepped == True:
            print("STEPPING TWICE")
        self.stepped = True
