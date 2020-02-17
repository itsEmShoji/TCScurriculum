import sys

# TODO: the coordinate system

# TODO: lets first create a set of all the squares
assert(len(squares) == 81)  # there are 81 squares

# TODO: now we will collect all the units together for checking validity
assert(len(all_units) == 27)  # there are 27 units

# TODO: we can now map each square to its units
# TODO: each square should belong to three units, its row, column, and block
assert(all(len(units[s]) == 3 for s in squares))

# TODO: peers are the set of squares that share units
assert(all(len(peers[s]) == 20 for s in squares))


def assign(solution, square, value):
    """
    Assign a value to a given square.
    :param solution: current solution for grid
    :param square: square to assign
    :param value: value to assign
    """

    # TODO: We must eliminate this value from the other squares that this square's peer because they're no longer an option
    pass


def eliminate(solution, square, value):
    """
    Conduct constraint propagation
    Eliminate the value from all the peer squares as a possibility and then conclude what is possible then
    :param solution: current solution for sudoku grid
    :param square: coordinates for square in question
    :param value: value to eliminate for the square
    """
    pass


def is_filled(solution):
    """
    Determines if all the squares only have one option remaining
    :param solution: current solution for the grid
    :return: True if all squares are filled, False otherwise meaning more searching needed
    """
    return all(len(solution[s]) == 1 for s in squares)


def search(solution):
    """
    Perform a search for solutions if constraint propagation failed.
    :param solution: current solution for the grid
    :return: True if a solution is reached, False if not
    """
    pass


def print_grid(grid):
    """
    Print the grid prettily
    :param grid: the sudoku
    :return:
    """
    max_len = max(len(grid[s]) for s in squares if grid[s])
    for r in rows:
        for c in cols:
            print('{val:^{width}} '.format(
                val=grid[r+c] if grid[r+c] else '-', width=max_len), end='')
        print()


# an example puzzle
puzzle = '''4.....8.5
            .3.......
            ...7.....
            .2.....6.
            ....8.4..
            ....1....
            ...6.3.7.
            5..2.....
            1.4......'''


def parse_puzzle(position):
    """
    Construct our data type from a string
    :param position:
    :return:
    """
    pass


if __name__ == '__main__':
    pass
