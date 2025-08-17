import numpy as np
import random

def generate_grid(size, obstacle_density):
    """
    generates grid with given size, obstacles
    """
    grid = np.zeros((size, size), dtype=int)
    obstacle_count = int(size * size * obstacle_density)
    obstacles = random.sample([(x, y) for x in range(size) for y in range(size)], obstacle_count)
    for (x, y) in obstacles:
        grid[x, y] = 1
    return grid

def easy_grid(size):
    return generate_grid(size, obstacle_density=0.1)

def medium_grid(size):
    return generate_grid(size, obstacle_density=0.25)

def hard_grid(size):
    return generate_grid(size, obstacle_density=0.4)