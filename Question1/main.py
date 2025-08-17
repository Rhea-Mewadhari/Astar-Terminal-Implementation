import time
from grid_generator import easy_grid, medium_grid, hard_grid
from astar import astar
from visualiser import print_grid

def run_scenario(grid_func, size, label):
    print(f"\n {label.upper()} GRID")

    grid = grid_func(size)

    start = (0, 0)
    goal = (size - 1, size - 1)

    grid[start[0], start[1]] = 0
    grid[goal[0], goal[1]] = 0

    start_time = time.time()
    path, explored, cost = astar(grid, start, goal)
    end_time = time.time()

    if path:
        print(f"Path found with cost: {cost}")
    else:
        print("No path found.")

    print(f"Nodes explored: {len(explored)}")
    print(f"Time taken: {end_time - start_time:.4f} seconds")
    print_grid(grid, path=path, explored=explored, start=start, goal=goal)

def main():
    grid_size = 15  # You can change this if desired

    run_scenario(easy_grid, grid_size, "Easy")
    run_scenario(medium_grid, grid_size, "Medium")
    run_scenario(hard_grid, grid_size, "Hard")

if __name__ == "__main__":
    main()