def print_grid(grid, path=None, explored=None, start=None, goal=None):
    """
    [] = obstacle
    *  = optimal path
    -  = explored node (but not in path)
    S  = start
    G  = goal
    """
    size = grid.shape[0]
    path_set = set(path) if path else set()
    explored_set = set(explored) if explored else set()

    for i in range(size):
        row = ""
        for j in range(size):
            cell = (i, j)
            if cell == start:
                row += " S "
            elif cell == goal:
                row += " G "
            elif grid[i, j] == 1:
                row += "[] "
            elif cell in path_set:
                row += " * "
            elif cell in explored_set:
                row += " - "
            else:
                row += " . "
        print(row)