import uuid
from dataclasses import dataclass, field
from model.enums.maze_wall import MazeWall

@dataclass(eq=False)
class MazeCell:
    x: int
    y: int
    walls: int = 0
    _uuid: uuid.UUID = field(default_factory=uuid.uuid4, init=False)

    def open_wall(self, cell_wall: MazeWall):
        self.walls |= cell_wall.bit_val

    def is_open(self, maze_wall: MazeWall) -> bool:
        return (maze_wall.bit_val & self.walls) == maze_wall.bit_val

    def __hash__(self):
        return hash(self._uuid)

    def __eq__(self, other):
        if not isinstance(other, MazeCell):
            return False
        return self._uuid == other._uuid
