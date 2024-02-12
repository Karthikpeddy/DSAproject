import random
from collections import deque

# Define the characters
WALL = "▓"
OPEN_SPACE = "◌"
START = "S"
END = "E"
PATH = "◍"

# Maze Generation Function
def generate_maze(n, p):
    maze = [[OPEN_SPACE]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if random.random() < p:
                maze[i][j] = WALL
    maze[0][0] = START
    maze[n-1][n-1] = END
    return maze

# Maze Printing Function
# Maze Printing Function
def print_maze(maze):
    for row in maze:
        for cell in row:
            if cell == START:
                print('\033[94m' + cell + '\033[0m', end='')  # Blue
            elif cell == END:
                print('\033[92m' + cell + '\033[0m', end='')  # Green
            elif cell == WALL:
                print('\033[91m' + cell + '\033[0m', end='')  # Red
            elif cell == OPEN_SPACE:
                print('\033[96m' + cell + '\033[0m', end='')  # Cyan
            elif cell == PATH:
                print('\033[92m' + cell + '\033[0m', end='')  # Green
        print()
    print()

# Pathfinding Function
def solve_maze(maze):
    n = len(maze)
    visited = [[False]*n for _ in range(n)]
    queue = deque([(0, 0, [])])
    while queue:
        x, y, path = queue.popleft()
        if (x, y) == (n-1, n-1):
            return path + [(x, y)]
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[ny][nx] and maze[ny][nx] != WALL:
                queue.append((nx, ny, path + [(x, y)]))
                visited[ny][nx] = True
    return None


# Path Marking Function
def mark_path(maze, path):
    for x, y in path:
        if maze[y][x] != START and maze[y][x] != END:
            maze[y][x] = PATH
    return maze

# Main Function
def main():
    size = int(input("Enter the size of the maze (n): "))
    maze = generate_maze(size, 0.25)
    print("\nGenerated Maze:")
    print_maze(maze)

    while True:
        print("\nOptions:")
        print("1. Print Path")
        print("2. Generate Another Puzzle")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            path = solve_maze([row[:] for row in maze])
            if path:
                marked_maze = mark_path([row[:] for row in maze], path)
                print("\nPath:")
                print_maze(marked_maze)
            else:
                print("No path found.")
        elif choice == '2':
            maze = generate_maze(size, 0.25)
            print("\nGenerated Maze:")
            print_maze(maze)
        elif choice == '3':
            print("Exiting. Thank you for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()