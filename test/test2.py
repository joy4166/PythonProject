import random

def generate_maze(width, height):
    maze = [["#" for _ in range(width)] for _ in range(height)]

    def dfs(x, y):
        maze[y][x] = " "
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx * 2, y + dy * 2
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == "#":
                maze[y + dy][x + dx] = " "
                dfs(nx, ny)

    dfs(1, 1)  # 시작점

    # Ending point
    maze[height - 2][width - 2] = "E"

    return maze

def print_maze(maze):
    for row in maze:
        print("".join(row))

if __name__ == "__main__":
    width = 20  # 미로의 가로 길이
    height = 10  # 미로의 세로 길이

    maze = generate_maze(width, height)
    print_maze(maze)
