from enum import Enum

class MazeWall(Enum):
    TOP = (0b0001, 1, 0, -1)
    DOWN = (0b0010, 0, 0, 1)
    LEFT = (0b0100, 3, -1, 0)
    RIGHT = (0b1000, 2, 1, 0)

    def __init__(self, bit_val, opposite_ordinal, diff_x, diff_y):
        self.bit_val = bit_val
        self.opposite_ordinal = opposite_ordinal
        self.diff_x = diff_x
        self.diff_y = diff_y

    def get_opposite(self):
        return list(MazeWall)[self.opposite_ordinal]
