import time
from model.enums.maze_wall import MazeWall
from model.maze_solution import MazeSolution
from solvers.maze_solver import MazeSolver

class TreeMazeSolver(MazeSolver):
    def solve(self, maze, maze_viewer, speed: float) -> MazeSolution:
        possibilities = []
        current_path = []
        visited = set()
        current_head = maze.maze_cells_array[0][0]

        while not self.is_finish(maze, current_head):
            visited.add(current_head)
            maze_viewer.highlight_cells(current_path)
            maze_viewer.check_events()
            time.sleep(speed / 1000.0)
            neighbours = self.get_neighbours(maze, current_head, visited)
            if not neighbours:
                if current_path:
                    current_head = current_path.pop()
                else:
                    break
                continue
            current_path.append(current_head)
            possibilities.extend(neighbours)
            current_head = possibilities.pop()
        current_path.append(current_head)
        maze_viewer.highlight_cells(current_path)
        return MazeSolution(correct_path=current_path)

    def get_neighbours(self, maze, current_head, visited):
        neighbours = []
        for wall in MazeWall:
            nx = current_head.x + wall.diff_x
            ny = current_head.y + wall.diff_y
            if maze.is_out_of_bounds(nx, ny):
                continue
            neighbor = maze.maze_cells_array[nx][ny]
            if not current_head.is_open(wall):
                continue
            if neighbor in visited:
                continue
            neighbours.append(neighbor)
        return neighbours
