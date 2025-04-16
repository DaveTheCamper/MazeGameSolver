from abc import ABC, abstractmethod
from model.maze import Maze
from model.maze_cell import MazeCell
from model.maze_solution import MazeSolution
from maze_viewer import MazeViewer


class MazeSolver(ABC):
    @abstractmethod
    def solve(self, maze: Maze, maze_viewer: "MazeViewer", speed: float) -> MazeSolution:
        """
        Resolve o labirinto e atualiza a exibição.
        :param maze: A instância do labirinto.
        :param maze_viewer: O objeto de visualização (atualizado durante a resolução).
        :param speed: A velocidade (em milissegundos) de atualização.
        :return: Um objeto MazeSolution com o caminho correto.
        """
        pass

    def is_finish(self, maze: Maze, maze_cell: MazeCell) -> bool:
        finish = maze.size - 1
        return maze_cell.x == finish and maze_cell.y == finish
