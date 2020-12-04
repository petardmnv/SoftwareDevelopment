from typing import List


class Turtle:
    canvas: List[List[int]]
    x: int
    y: int
    is_spawned: bool
    orientation: str

    def __init__(self, x: int, y: int):
        self.row = x
        self.column = y
        self.x = 0
        self.y = 0
        self.canvas = [[0] * y for i in range(x)]
        self.is_spawned = False
        self.orientation = "right"

    def spawn_at(self, row: int, column: int):
        self.is_spawned = True
        self.x = row
        self.y = column
        self.canvas[self.x][self.y] += 1

    def move(self):
        if not self.is_spawned:
            raise RuntimeError

        orientations: dict = {"left": [0, -1], "up": [-1, 0], "right": [0, 1], "down": [1, 0]}
        x, y = orientations[self.orientation]
        self.x += x
        self.y += y
        self.transfer()
        self.canvas[self.x][self.y] += 1

    def transfer(self):
        if self.x < 0:
            self.x = self.row - 1
        elif self.x >= self.row:
            self.x = 0
        if self.y < 0:
            self.y = self.column - 1
        elif self.y >= self.column:
            self.y = 0

    def turn_right(self):
        orientations: tuple = ("left", "up", "right", "down")
        index: int = orientations.index(self.orientation) + 1
        if index >= len(orientations):
            index = 0
        self.orientation =\
            orientations[index]

    def turn_left(self):
        orientations: tuple = ("left", "up", "right", "down")
        index: int = orientations.index(self.orientation) -1
        if index < 0:
            index = len(orientations) - 1
        self.orientation =\
            orientations[index]


class SimpleCanvas:
    canvas: List[List[int]]
    symbols: List[str]

    def __init__(self, canvas: list, symbols: list):
        self.symbols = symbols
        self.canvas = canvas

    def draw(self): #-> str:
        canvas_rows: int = len(self.canvas)
        canvas_columns: int = len(self.canvas[0])
        pixels_count: int = sum([self.canvas[i][j] for j in range(canvas_columns) for i in range(canvas_rows)])

        pixelized_cnavas: List[List[float]] = [[0.00] * canvas_columns for i in range(canvas_rows)]
        for i in range(canvas_rows):
            for j in range(canvas_columns):
                pixelized_cnavas[i][j] = self.canvas[i][j] / pixels_count
        return pixelized_cnavas


turtle = Turtle(3, 3)
turtle.spawn_at(0, 0)
for i in range(9):
    turtle.move()
turtle.turn_right()
for i in range(4):
    turtle.move()
turtle.turn_left()
turtle.move()
turtle.move()
turtle.turn_right()
turtle.move()
print(turtle.canvas)
canvas = SimpleCanvas(turtle.canvas, [' ', '*', '@', '#'])
print(canvas.draw())