from time import sleep


def next_generation(grid):
    new_grid = [[0 for i in range(15)] for k in range(15)]
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            new_grid[row][col] = grid[row][col]
            neighbours = check_cell(grid, row, col)
            if grid[row][col]:
                if neighbours != 2 and neighbours != 3:
                    new_grid[row][col] = 0
            else:
                if neighbours == 3:
                    new_grid[row][col] = 1

    return new_grid


def check_cell(grid, row, column):
    neighbours = 0
    limit = 15
    moves = (
        [1, 0],
        [0, 1],
        [-1, 0],
        [0, -1],
        [1, 1],
        [1, -1],
        [-1, 1],
        [-1, -1]
    )
    for move in moves:
        new_row = row + move[0]
        new_column = column + move[1]
        if new_row < 0 or new_row >= limit or new_column < 0 or new_column >= limit:
            continue
        if grid[new_row][new_column]:
            neighbours += 1
        if neighbours >= 4:
            break
    return neighbours


def print_grid(grid):
    for row in grid:
        for cell in row:
            print('■' if cell else '□', end=' ')
        print('')


def animate(grid):
    generation = grid
    while True:
        print('')
        print('')
        print_grid(generation)
        sleep(1)
        generation = next_generation(generation)


g = [[0 for i in range(15)] for k in range(15)]
g[0][0] = 1
g[0][1] = 1
g[0][2] = 1

animate(g)