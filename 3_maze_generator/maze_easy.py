import random
import queue

# Maze generator based on work by Christian Hill in April 2017,
# see the original at https://scipython.com/blog/making-a-maze/
# Code was extended by Marcus Hughes, March 2020
#
# Mazes are generated using the depth-first algorithm.
# Maze solver uses the breadth-first algorithm to create a solution. Written by Marcus Hughes, March 2020.


class Cell:
    """A cell in the maze.

    A maze "Cell" is a point in the grid which may be surrounded by walls to
    the north, east, south or west.
    """
    # A wall separates a pair of cells in the N-S or W-E directions.
    wall_pairs = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}

    def __init__(self, x, y):
        """Initialize the cell at (x,y). At first it is surrounded by walls."""
        self.x, self.y = x, y
        self.walls = {'N': True, 'S': True, 'E': True, 'W': True}

    def has_all_walls(self):
        """Does this cell still have all its walls?"""
        return all(self.walls.values())

    def knock_down_wall(self, other, wall):
        """Knock down the wall between cells self and other."""
        self.walls[wall] = False
        other.walls[Cell.wall_pairs[wall]] = False


class Maze:
    """A Maze, represented as a grid of cells."""

    def __init__(self, nx, ny, ix=0, iy=0, ex=None, ey=None):
        """Initialize the maze grid.
        The maze consists of nx x ny cells and will be constructed starting
        at the cell indexed at (ix, iy).
        """
        self.nx, self.ny = nx, ny
        self.ix, self.iy = ix, iy

        # Setup the ending position
        if ex is None or ey is None:
            self.ex, self.ey = nx-1, ny-1
        else:
            self.ex, self.ey = ex, ey

        # Construct the maze array
        self.maze_map = [[Cell(x, y) for y in range(ny)] for x in range(nx)]

    def cell_at(self, x, y):
        """Return the Cell object at (x,y)."""
        return self.maze_map[x][y]

    def __str__(self):
        """Return a (crude) string representation of the maze."""
        maze_rows = ['-' * self.nx*2]
        for y in range(self.ny):
            maze_row = ['|']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['E']:
                    maze_row.append(' |')
                else:
                    maze_row.append('  ')
            maze_rows.append(''.join(maze_row))
            maze_row = ['|']
            for x in range(self.nx):
                if self.maze_map[x][y].walls['S']:
                    maze_row.append('-+')
                else:
                    maze_row.append(' +')
            maze_rows.append(''.join(maze_row))
        return '\n'.join(maze_rows)

    def write_svg(self, filename, solution=None):
        """Write an SVG image of the maze to filename."""

        aspect_ratio = self.nx / self.ny
        # Pad the maze all around by this amount.
        padding = 10
        # Height and width of the maze image (excluding padding), in pixels
        height = 500
        width = int(height * aspect_ratio)
        # Scaling factors mapping maze coordinates to image coordinates
        scy, scx = height / self.ny, width / self.nx

        def write_wall(f, x1, y1, x2, y2):
            """Write a single wall to the SVG image file handle f."""

            print(
                '<line x1="{}" y1="{}" x2="{}" y2="{}"/>'.format(x1, y1, x2, y2), file=f)

        # Write the SVG image file for maze
        with open(filename, 'w') as f:
            # SVG preamble and styles.
            print('<?xml version="1.0" encoding="utf-8"?>', file=f)
            print('<svg xmlns="http://www.w3.org/2000/svg"', file=f)
            print('    xmlns:xlink="http://www.w3.org/1999/xlink"', file=f)
            print('    width="{:d}" height="{:d}" viewBox="{} {} {} {}">'
                  .format(width+2*padding, height+2*padding, -padding, -padding, width+2*padding, height+2*padding),
                  file=f)
            print('<defs>\n<style type="text/css"><![CDATA[', file=f)
            print('line {', file=f)
            print('    stroke: #000000;\n    stroke-linecap: square;', file=f)
            print('    stroke-width: 5;\n}', file=f)
            print(']]></style>\n</defs>', file=f)

            # Draw the solution if provided
            if solution:
                for (x, y) in solution:
                    print('<rect x="{}" y="{}" width="{}" height="{}" style="fill:rgb(0,255,0)" />'.
                          format(x * scx, y * scy, scx, scy), file=f)

            # Draw colored squares for the start and end positions
            print('<rect x="{}" y="{}" width="{}" height="{}" style="fill:rgb(0,0,255)" />'.
                  format(self.ix*scx, self.iy*scy, scx, scy), file=f)
            print('<rect x="{}" y="{}" width="{}" height="{}" style="fill:rgb(255,0,0)" />'.
                  format(self.ex * scx, self.ey * scy, scx, scy), file=f)

            # Draw the "South" and "East" walls of each cell, if present (these
            # are the "North" and "West" walls of a neighbouring cell in
            # general, of course).
            for x in range(self.nx):
                for y in range(self.ny):
                    if maze.cell_at(x, y).walls['S']:
                        x1, y1, x2, y2 = x*scx, (y+1)*scy, (x+1)*scx, (y+1)*scy
                        write_wall(f, x1, y1, x2, y2)
                    if maze.cell_at(x, y).walls['E']:
                        x1, y1, x2, y2 = (x+1)*scx, y*scy, (x+1)*scx, (y+1)*scy
                        write_wall(f, x1, y1, x2, y2)

            # Draw the North and West maze border, which won't have been drawn
            # by the procedure above.
            print('<line x1="0" y1="0" x2="{}" y2="0"/>'.format(width), file=f)
            print('<line x1="0" y1="0" x2="0" y2="{}"/>'.format(height), file=f)

            print('</svg>', file=f)

    def find_valid_neighbours(self, cell):
        """
        Return a list of unvisited neighbours to cell.

        An example output:
        [("N", cell1), ("W", cell2)]
        Note: the list contains tuples of the direction of the neighbor and a handle to the actual neighboring cell
        """

        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]
        neighbours = []
        for direction, (dx, dy) in delta:
            # Determine the candidate neighbor's position
            x2, y2 = cell.x + dx, cell.y + dy

            # If it's a valid position, i.e. on the grid
            if (0 <= x2 < self.nx) and (0 <= y2 < self.ny):

                # Get the cell object and check if it is unvisited, i.e. it has all its walls.
                # If so, then append it to the neighbors list with its direction
                neighbour = maze.cell_at(x2, y2)
                if neighbour.has_all_walls():
                    neighbours.append((direction, neighbour))
        return neighbours

    def make_maze(self):
        """
        Construct a maze using a depth first search approach
        """
        # TODO: calculate total number of cells

        # TODO: create cell_stack to keep cells as processing using DFS

        # Start at the requested start position
        current_cell = self.cell_at(self.ix, self.iy)

        # TODO: Keep track of total number of visited cells during maze construction.

        # TODO: While not all the cells have been visited
          # Determine the neighbors of the current cell
          neighbours = self.find_valid_neighbours(current_cell)

           # TODO: If no neighbors exist,
           if not neighbours:
                # We've reached a dead end: backtrack.
                current_cell = cell_stack.pop()
                continue

            # Choose a random neighbouring cell and move to it.
            direction, next_cell = random.choice(neighbours)
            current_cell.knock_down_wall(next_cell, direction)
            # append the current cell so you can backtrack appropriately
            cell_stack.append(current_cell)
            current_cell = next_cell
            nv += 1


class MazeSolver:
    """
    Solves the Maze generated by the above class with BFS.
    """

    def __init__(self, maze):
        self.maze = maze
        self.start = (self.maze.ix, self.maze.iy)
        self.goal = (self.maze.ex, self.maze.ey)

    def get_reachable_neighbors(self, x, y):
        """
        Neighbors that can be reached from the cell (x, y)

        Checks for walls blocking the path and out-of-bounds movement
        """
        cell = self.maze.cell_at(x, y)
        # TODO: make an empty list to hold neighbors

        delta = [('W', (-1, 0)),
                 ('E', (1, 0)),
                 ('S', (0, 1)),
                 ('N', (0, -1))]

        for direction, (dx, dy) in delta:
            # If a cell doesn't have walls in that direction the neighbor is reachable.
            if not cell.walls[direction]:
                # Determine the candidate neighbor's position
                x2, y2 = cell.x + dx, cell.y + dy

                # If it's a valid position, i.e. on the grid
                if (0 <= x2 < self.maze.nx) and (0 <= y2 < self.maze.ny):
                    neighbors.append((x2, y2))
        return neighbors

    def solve(self):
        """
        Solves the maze using BFS.
        If no solution can be found it returns False.
        Otherwise, it returns the cells along the solution path.
        This solution path result can be passed to the write_svg method of Maze to show the solution.
        """
        # Create necessary data structures
        q = queue.Queue()  # keeps track of cells to visit
        visited_nodes = set()  # keeps track of cells already visited
        parents = dict()  # records the previous cell, i.e. parent in the BFS tree, visited when hunting for a solution

        # Initialize by putting the start in all
        q.put(self.start)
        visited_nodes.add(self.start)
        parents[self.start] = None

        # While there are cells remaining to visit
        while not q.empty():
            # Pop a cell off and get its neighbors
            current_cell = q.get()
            neighbors = self.get_reachable_neighbors(
                current_cell[0], current_cell[1])

            # For each unvisited neighbor, add it to the visited list, the q to move from, and assign its parent
            for neighbor in neighbors:
                if neighbor not in visited_nodes:
                    visited_nodes.add(neighbor)
                    q.put(neighbor)
                    parents[neighbor] = current_cell

                # If the neighbor happened to be the goal cell, quit and return the backtracked solution
                if current_cell == self.goal:
                    return self.backtrack(parents)

        # No path to the goal node was found
        return False

    def backtrack(self, parents):
        """
        Using information from the BFS search, works backward from the goal cell to determine how it was reached.
        Returns the solution path
        """

        # Starting at the goal node build up the path back to the starting cell
        current = self.goal
        path = [current]

        # While not at the starting cell
        while parents[current] is not None:
            # Determine how we got to this cell and walk backward
            path.append(parents[current])
            current = parents[current]
        return list(reversed(path))


if __name__ == "__main__":
    """ An example!"""
    # Maze dimensions (ncols, nrows)
    num_x, num_y = 5, 5
    # Maze entry position
    start_x, start_y = 0, 0

    maze = Maze(num_x, num_y, start_x, start_y)
    # TODO: call make maze on our maze

    print(maze)
    maze.write_svg('maze.svg')

    # TODO: make a mazeSolver object called solver
    # TODO: generate our solution path by calling solve on solver
    # TODO: print our solution path
    maze.write_svg('solution.svg', path)
