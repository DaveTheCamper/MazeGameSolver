import time
import heapq
import itertools
from model.enums.maze_wall import MazeWall
from model.maze_solution import MazeSolution
from solvers.maze_solver import MazeSolver

class AStarMazeSolver(MazeSolver):
    def solve(self, maze, maze_viewer, speed: float) -> MazeSolution:
        start = maze.maze_cells_array[0][0]
        goal  = maze.maze_cells_array[-1][-1]

        counter = itertools.count()

        open_set = []
        start_f = self.heuristic(start, goal)
        heapq.heappush(open_set, (start_f, next(counter), start))

        came_from  = {}
        g_score    = {start: 0}
        closed_set = set()

        while open_set:
            current_f, _, current = heapq.heappop(open_set)

            path = self._reconstruct_path(came_from, current)
            maze_viewer.highlight_cells(path)
            maze_viewer.check_events()
            time.sleep(speed / 1000.0)

            if self.is_finish(maze, current):
                return MazeSolution(correct_path=path)

            if current in closed_set:
                continue

            closed_set.add(current)

            for neighbor in self.get_neighbours(maze, current):
                if neighbor in closed_set:
                    continue

                tentative_g = g_score[current] + 1

                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, goal)                    # incluímos next(counter) para desempatar
                    heapq.heappush(open_set, (f_score, next(counter), neighbor))

        return MazeSolution(correct_path=[])

    def heuristic(self, cell, goal) -> int:
        return abs(cell.x - goal.x) + abs(cell.y - goal.y)

    def get_neighbours(self, maze, current):
        neighbours = []
        for wall in MazeWall:
            nx = current.x + wall.diff_x
            ny = current.y + wall.diff_y

            if maze.is_out_of_bounds(nx, ny):
                continue

            neighbor = maze.maze_cells_array[nx][ny]

            if not current.is_open(wall):
                continue

            neighbours.append(neighbor)
        return neighbours

    def _reconstruct_path(self, came_from, current):
        path = [current]

        while current in came_from:
            current = came_from[current]
            path.append(current)

        return list(reversed(path))
