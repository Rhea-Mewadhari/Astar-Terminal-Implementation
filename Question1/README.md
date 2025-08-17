# A* Pathfinding Visualizer (Terminal-Based)

This project implements the **A\*** search algorithm in a 2D grid environment, simulating a mobile robot navigating from a **start** to a **goal** while avoiding obstacles.


## Features

- A* Search Algorithm with **Manhattan Distance**
- Adjustable obstacle **density levels**:
  - Easy (10%)
  - Medium (25%)
  - Hard (40%)
- Terminal visualization using:
  - `[]` → obstacle
  - `*` → path taken
  - `-` → explored but not chosen
  - `.` → free cell
  - `S` / `G` → start / goal
- Reports:
  - Nodes explored
  - Total path cost
  - Time taken to compute

### 🧰 Requirements
- Python


## How to Run:

1. Pull this repo down.
2. Create a venv:
```
python -m venv venv
```
3. Activate the virtual environment:
```
venv\Scripts\Activate.ps1
```
4. Install required libraries:
```
pip install -r requirements.txt
```
5. Run the program:
```
python main.py
```

Inspect the terminal to see the out come.