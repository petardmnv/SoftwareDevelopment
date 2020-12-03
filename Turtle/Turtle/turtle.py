from typing import List


class Turtle:
    canvas: List[List[int]]
    x: int
    y: int
    is_spawned: bool
    orientation: str

    def __init__(self, x, y):
        self.row = x
        self.column = y
        self.x = 0
        self.y = 0
        self.canvas = [[0] * y for i in range(x)]
        self.is_spawned = False
        self.orientation = "right"

    def spawn_at(self, row, column):
        self.is_spawned = True
        self.x = row
        self.y = column
        self.canvas[self.x][self.y] += 1

    def move(self):
        if not self.is_spawned:
            raise RuntimeError

        orientations = {"left": [0, -1], "up": [-1, 0], "right": [0, 1], "down": [1, 0]}
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
        orientations = ("left", "up", "right", "down")
        index = orientations.index(self.orientation) + 1
        if index >= len(orientations):
            index = 0
        self.orientation =\
            orientations[index]

    def turn_left(self):
        orientations = ("left", "up", "right", "down")
        index = orientations.index(self.orientation) -1
        if index < 0:
            index = len(orientations) - 1
        self.orientation =\
            orientations[index]


class SimpleCanvas:
    pass


turtle = Turtle(3, 3)
turtle.spawn_at(0, 0)
turtle.move()
turtle.turn_right()
turtle.move()
turtle.move()
turtle.turn_left()
turtle.move()
turtle.move()
turtle.turn_right()
turtle.move()
print(turtle.canvas)
