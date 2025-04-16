from dataclasses import dataclass
from typing import List
from model.maze_cell import MazeCell

@dataclass
class MazeSolution:
    correct_path: List[MazeCell]