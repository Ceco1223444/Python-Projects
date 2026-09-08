class Maze:
    # Visualization characters
    block = "\uFF03"
    empty = "\u3000"
    path = "\uFF0A"
    def __init__(self, start, transitions):
        """ A maze has a start and a tree structure representing all possible transitions """
        self.start = start
        self.transitions = transitions
        # Build visual representation
        width = max(self.transitions, key=lambda x: x[0])[0]
        height = max(self.transitions, key=lambda x: x[1])[1]
        self.maze = [[Maze.block] * (width + 3), [Maze.block] * (width + 3)]
        for j in range(height + 1):
            row = [Maze.block, Maze.block]
            for i in range(width + 1):
                row.append(Maze.empty if (i, j) in self.transitions else Maze.block)
            row.append(Maze.block)
            self.maze.append(row)
        self.maze.append([Maze.block] * (width + 3))
    def __repr__(self):
        """ Returns a string representation of the maze """
        return '\n'.join([''.join(row) for row in self.maze])
    def show(self, route):
        """ Shows the maze with the solution route """
        maze_copy = [row.copy() for row in self.maze]
        for pos in route:
            maze_copy[pos[1] + 1][pos[0] + 1] = Maze.path
        print('\n'.join([''.join(row) for row in maze_copy]))
def find_route_rec(maze, current, end, path=None):
    """ Recursive helper function to find a path from current to end """
    if path is None:
        path = []
    path.append(current)
    if current == end:
        return path
    for neighbor in maze.transitions.get(current, []):
        if neighbor not in path:
            result = find_route_rec(maze, neighbor, end, path.copy())
            if result:
                return result
    return None
def find_route(maze, end):
    """ Finds a route from maze.start to end """
    route = find_route_rec(maze, maze.start, end)
    if route is None:
        print("Warning: no route can be found!")
        return []
    return route
# Demo script
if __name__ == "__main__":
    # Example maze
    example_maze_transitions = {
        (0, 0): [(0, 1), (1, 0)],
        (0, 1): [(0, 0), (0, 2)],
        (0, 2): [(0, 1), (1, 2)],
        (1, 0): [(0, 0), (1, 1)],
        (1, 1): [(1, 0), (1, 2)],
        (1, 2): [(1, 1), (0, 2)],
    }
    start = (0, 0)
    end = (1, 2)
    maze = Maze(start, example_maze_transitions)
    print("Maze representation:")
    print(maze)
    route = find_route(maze, end)
    print("\nSolution route:")
    print(route)
    maze.show(route)
