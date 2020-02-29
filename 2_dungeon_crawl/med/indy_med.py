
import sys
from Coordinate import Coordinate
from SmartDeque import SmartDeque


def main():
    # TODO: Store the method we are using to solve (s|q)
    # TODO: Store the name of the dungeo file we are searching
    # TODO: Read from file & store the dungeon map
    # TODO: Store N (the size of the room)
    # TODO: Store R (the number of rooms)
    # TODO: Create a list to store our solution
    # TODO: create a SmartDeque object as our pathfinder

    # TODO: Find our starting point - Create a double for loop to iterate through our maze (use N & L)
    # use i as our first variable and j as the second
            print(temple_map[i][j])
            # TODO: Create another for loop through N using k as our variable
                if temple_map[i][j][k].value == 'j':
                    temple_map[i][j][k].step()
                    # TODO: put our starting point (temple_map[i][j][k]) into our pathfinder

    # TODO: Create a variable to keep track of whether our map is solvable
    ticker = 0

   # TODO: Create a infinite loop
        ticker += 1
        # TODO: Check if our pathfinder is empty - this means we have no solution
            print("No Solution")
            # TODO: set solvable to false
            # TODO: break from our infinite loop
        # TODO: Create variable 'current' to keep track of which location we are searching from
        print(f"considering ({current.level},{current.row},{current.col})")
        # TODO: if our current is ever 'a', we have found the artifact & therefore a solution
            # TODO:Append current to our final solution
            print("FOUND IT!")
            # TODO: Break from the infinite loop
        # TODO: pop from our pathfinder to update current & search from a new spot

        # TODO: check if our current value is 'r' (a rope)
            # UP
            # TODO: check if we are at the lowest level (room R-1)
                up_cord = current.get_neighbor('u', temple_map)
                if up_cord.is_walkable():
                    up_cord.step()
                    up_cord.prev = 'd'
                    pathfinder.push(up_cord)
            # DOWN
            # TODO: Check if we are able to continue down (as long as we aren't at level 0)
                down_cord = current.get_neighbor('d', temple_map)
                if down_cord.is_walkable():
                    down_cord.step()
                    down_cord.prev = 'u'
                    pathfinder.push(down_cord)
            pass
        # TODO: check if our current value is a ramp (> or <)
            # TODO: check if our ramp is going up to the right (<)
                # WEST
                if current.col != 0:
                    west_cord = current.get_neighbor('w', temple_map)
                    if west_cord.is_walkable():
                        west_cord.step()
                        west_cord.prev = 'e'
                        pathfinder.push(west_cord)
            # TODO: check our other ramp direction
                if current.col != N-1:
                    east_cord = current.get_neighbor('e', temple_map)
                    if east_cord.is_walkable():
                        east_cord.step()
                        east_cord.prev = 'w'
                        pathfinder.push(east_cord)

        # TODO: Check if current.value is'.' or 'j' (empty space or our starting point)
            # NORTH
            # TODO: Check if we are in the first row
                north_cord = current.get_neighbor('n', temple_map)
                if north_cord.is_walkable():
                    north_cord.step()
                    north_cord.prev = 's'
                    pathfinder.push(north_cord)
            # EAST
            # TODO: check if we are in the column furthest to the east (In column N-1)
                east_cord = current.get_neighbor('e', temple_map)
                if east_cord.is_walkable():
                    east_cord.step()
                    east_cord.prev = 'w'
                    pathfinder.push(east_cord)
            # SOUTH
            # TODO: Check if we are in the furthest row (Row N-1)
                south_cord = current.get_neighbor('s', temple_map)
                if south_cord.is_walkable():
                    south_cord.step()
                    south_cord.prev = 'n'
                    pathfinder.push(south_cord)
            # WEST
            # TODO:Check if we are in the first column
                west_cord = current.get_neighbor('w', temple_map)
                if west_cord.is_walkable():
                    west_cord.step()
                    west_cord.prev = 'e'
                    pathfinder.push(west_cord)

    # TODO: check if our map is solvable
        # TODO: create another infinite loop
            cur_pos = path[len(path) - 1]
            prev_pos = cur_pos.get_neighbor(cur_pos.prev, temple_map)
            path.append(prev_pos)
            if prev_pos.value == 'j':
                break
        # TODO:print our solution
    # TODO: loop through our path backwards
        print(f'({c.level},{c.row},{c.col})')
    # print(ticker)


def read_input(file_name):

    test_file = open(file_name, 'r')
    mode = test_file.readline().rstrip()
    room_size = int(test_file.readline().rstrip())
    num_levels = int(test_file.readline().rstrip())
    all_lines = test_file.readlines()
    all_lines = [line.rstrip() for line in all_lines]
    temple_map = init_map(room_size, num_levels)

    if mode == 'M':
        _tmap = [list(line) for line in all_lines if line[0] != '/']
        tmap = []
        for i in range(num_levels):
            tmap.append(_tmap[i*room_size:(i+1)*room_size])
        for level in range(num_levels):
            for r in range(room_size):
                for c in range(room_size):
                    elt = tmap[level][r][c]
                    coord = Coordinate(r, c, level, elt)
                    temple_map[level][r][c] = coord
    else:
        for level in range(num_levels):
            for r in range(room_size):
                for c in range(room_size):
                    coord = Coordinate(r, c, level, '.')
                    temple_map[level][r][c] = coord
        for line in all_lines:
            if line[0] != '/':
                data = line.split(": ")
                elt = data[1]
                coord = data[0]
                coord = coord[1:(len(coord)-1)].split(",")
                level, row, col = int(coord[0]), int(coord[1]), int(coord[2])
                temple_map[level][row][col].value = elt

    return temple_map


def init_map(N, L):
    return [[[None for k in range(N)] for j in range(N)] for i in range(L)]


if __name__ == '__main__':
    main()
