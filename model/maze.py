from dataclasses import dataclass
from typing import List, Set
from model.maze_cell import MazeCell

@dataclass
class Maze:
    maze_cells_array: List[List[MazeCell]]
    size: int

    def get_maze_cells(self) -> Set[MazeCell]:
        cells = set()
        for row in self.maze_cells_array:
            cells.update(row)
        return cells

    def is_out_of_bounds(self, x: int, y: int) -> bool:
        return x < 0 or x >= self.size or y < 0 or y >= self.size
