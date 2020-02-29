
import sys
from Coordinate import Coordinate
from SmartDeque import SmartDeque


def main():
    structure = sys.argv[1]
    file_name = sys.argv[2]
    temple_map = read_input(file_name)
    N = len(temple_map[0])  # each room is NxN
    R = len(temple_map)  # number of rooms
    path = []  # final solution
    pathfinder = SmartDeque(structure)
    for i in range(R):
        for j in range(N):
            print(temple_map[i][j])
            for k in range(N):
                if temple_map[i][j][k].value == 'j':
                    temple_map[i][j][k].step()
                    pathfinder.push(temple_map[i][j][k])

    solvable = True
    ticker = 0
    while True:
        ticker += 1
        if pathfinder.empty():
            print("No Solution")
            solvable = False
            break
        current = pathfinder.front()
        print(f"considering ({current.level},{current.row},{current.col})")
        if(current.value == 'a'):
            path.append(current)
            print("FOUND IT!")
            break
        pathfinder.pop()

        if current.value == 'r':
            # UP
            if current.level != R-1:
                up_cord = current.get_neighbor('u', temple_map)
                if up_cord.is_walkable():
                    up_cord.step()
                    up_cord.prev = 'd'
                    pathfinder.push(up_cord)
            # DOWN
            if current.level != 0:
                down_cord = current.get_neighbor('d', temple_map)
                if down_cord.is_walkable():
                    down_cord.step()
                    down_cord.prev = 'u'
                    pathfinder.push(down_cord)
            pass
        elif current.value == '<' or current.value == '>':
            if current.value == '<':
                # WEST
                if current.col != 0:
                    west_cord = current.get_neighbor('w', temple_map)
                    if west_cord.is_walkable():
                        west_cord.step()
                        west_cord.prev = 'e'
                        pathfinder.push(west_cord)
            elif current.value == '>':
                if current.col != N-1:
                    east_cord = current.get_neighbor('e', temple_map)
                    if east_cord.is_walkable():
                        east_cord.step()
                        east_cord.prev = 'w'
                        pathfinder.push(east_cord)

        elif current.value == '.' or current.value == 'j':
            # NORTH
            if current.row != 0:
                north_cord = current.get_neighbor('n', temple_map)
                if north_cord.is_walkable():
                    north_cord.step()
                    north_cord.prev = 's'
                    pathfinder.push(north_cord)
            # EAST
            if current.col != N-1:
                east_cord = current.get_neighbor('e', temple_map)
                if east_cord.is_walkable():
                    east_cord.step()
                    east_cord.prev = 'w'
                    pathfinder.push(east_cord)
            # SOUTH
            if current.row != N-1:
                south_cord = current.get_neighbor('s', temple_map)
                if south_cord.is_walkable():
                    south_cord.step()
                    south_cord.prev = 'n'
                    pathfinder.push(south_cord)
            # WEST
            if current.col != 0:
                west_cord = current.get_neighbor('w', temple_map)
                if west_cord.is_walkable():
                    west_cord.step()
                    west_cord.prev = 'e'
                    pathfinder.push(west_cord)

    if solvable:
        while True:
            cur_pos = path[len(path) - 1]
            prev_pos = cur_pos.get_neighbor(cur_pos.prev, temple_map)
            path.append(prev_pos)
            if prev_pos.value == 'j':
                break
        print(path)
    for c in reversed(path):
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
