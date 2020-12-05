from typing import List


# KISS
class Turtle:
    canvas: List[List[int]]
    x: int
    y: int
    is_spawned: bool
    orientation: str

    def __init__(self, x: int, y: int):
        if x <= 0 or y <= 0:
            raise IndexError
        self.row = x
        self.column = y
        self.canvas = [[0] * y for i in range(x)]
        self.is_spawned = False
        self.orientation = "right"

    def spawn_at(self, row: int, column: int):
        if (row < 0) and (row >= self.row):
            raise IndexError
        if (column < 0) and (column >= self.column):
            raise IndexError
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
        self.x, self.y = self.transfer(self.x, self.y)
        self.canvas[self.x][self.y] += 1

    # ugly :'(
    def transfer(self, x, y) -> list:
        if x < 0:
            x = self.row - 1
        elif x >= self.row:
            x = 0
        if y < 0:
            y = self.column - 1
        elif y >= self.column:
            y = 0
        return [x, y]

    def turn_right(self):
        orientations: tuple = ("left", "up", "right", "down")
        index: int = orientations.index(self.orientation) + 1
        if index >= len(orientations):
            index = 0
        self.orientation = orientations[index]

    def turn_left(self):
        orientations: tuple = ("left", "up", "right", "down")
        index: int = orientations.index(self.orientation) - 1
        if index < 0:
            index = len(orientations) - 1
        self.orientation = orientations[index]


class SimpleCanvas:
    canvas: List[List[int]]
    symbols: List[str]

    def __init__(self, canvas: list, symbols: list):
        self.symbols = symbols
        self.canvas = canvas

    def draw(self) -> str:
        canvas_rows: int = len(self.canvas)
        canvas_columns: int = len(self.canvas[0])
        pixels_count: int = max([self.canvas[i][j] for j in range(canvas_columns) for i in range(canvas_rows)])

        pixelated_canvas: List[List[float]] = [[0.00] * canvas_columns for i in range(canvas_rows)]
        draw_canvas: List[List[str]] = [[""] * canvas_columns for i in range(canvas_rows)]

        symbols_range: float = 1 / (len(self.symbols) - 1)
        for i in range(canvas_rows):
            for j in range(canvas_columns):
                pixelated_canvas[i][j] = self.canvas[i][j] / pixels_count

                # drawing canvas
                if 0 == pixelated_canvas[i][j]:
                    draw_canvas[i][j] = self.symbols[0]

                for k in range(len(self.symbols) - 2):
                    if (k * symbols_range < pixelated_canvas[i][j]) and \
                            ((k + 1) * symbols_range >= pixelated_canvas[i][j]):
                        draw_canvas[i][j] = self.symbols[k + 1]

                if ((1 - symbols_range) < pixelated_canvas[i][j]) and (1 >= pixelated_canvas[i][j]):
                    draw_canvas[i][j] = self.symbols[len(self.symbols) - 1]

        return self.format_canvas(draw_canvas)

    @staticmethod
    def format_canvas(canvas: List[List[str]]) -> str:
        result: list = []
        for i in range(len(canvas)):
            result.append(''.join(canvas[i]))
        return '\n'.join(result)
