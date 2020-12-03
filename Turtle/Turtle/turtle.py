from typing import List


class Turtle:
    canvas: List[List[int]]
    x: int
    y: int
    is_spawned: bool

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.canvas = [[0, 0, 0] for i in range(3)]
        self.is_spawned = False

    def spawn_at(self, row, column):
        self.is_spawned = True
        self.x = row
        self.y = column
        self.canvas[self.x][self.y] += 1


class SimpleCanvas:
    pass
