import heapq
from utils import manhattan_distance

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position  
        self.parent = parent      
        self.g = g                
        self.h = h                
        self.f = g + h            

    def __lt__(self, other):
        return self.f < other.f

def get_neighbors(position, grid):
    """
    returns neighbor positions (up, down, left, right)
    """
    neighbors = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # N, S, W, E
    x, y = position
    rows, cols = grid.shape

    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < rows and 0 <= ny < cols and grid[nx, ny] == 0:
            neighbors.append((nx, ny))

    return neighbors

def astar(grid, start, goal):
    """
    A* algorithm to find the shortest path
    """
    open_set = []
    start_node = Node(start, g=0, h=manhattan_distance(start, goal))
    heapq.heappush(open_set, start_node)

    visited = set()
    explored_nodes = set()

    while open_set:
        current_node = heapq.heappop(open_set)
        current_pos = current_node.position

        if current_pos in visited:
            continue

        visited.add(current_pos)
        explored_nodes.add(current_pos)

        if current_pos == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1], explored_nodes, len(path) - 1 

        for neighbor_pos in get_neighbors(current_pos, grid):
            if neighbor_pos in visited:
                continue

            g = current_node.g + 1
            h = manhattan_distance(neighbor_pos, goal)
            neighbor_node = Node(neighbor_pos, parent=current_node, g=g, h=h)
            heapq.heappush(open_set, neighbor_node)

    return None, explored_nodes, float("inf")  # no path found