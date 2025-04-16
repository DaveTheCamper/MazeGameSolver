import random
from model.maze import Maze
from model.maze_cell import MazeCell
from model.enums.maze_wall import MazeWall

class MazeFactory:
    def create_maze(self, size: int) -> Maze:
        interactions = 0
        cells = self._create_initial_maze_walls(size)
        visited = [[False for _ in range(size)] for _ in range(size)]
        stack = [(0, 0)]
        visited[0][0] = True

        while stack:
            x, y = stack[-1]
            unvisited_neighbors = self._find_unvisited_neighbors(x, y, size, visited)
            if unvisited_neighbors:
                wall = random.choice(unvisited_neighbors)
                nx, ny = x, y
                if wall == MazeWall.TOP:
                    ny = y - 1
                elif wall == MazeWall.DOWN:
                    ny = y + 1
                elif wall == MazeWall.LEFT:
                    nx = x - 1
                elif wall == MazeWall.RIGHT:
                    nx = x + 1
                cells[x][y].open_wall(wall)
                cells[nx][ny].open_wall(wall.get_opposite())
                visited[nx][ny] = True
                stack.append((nx, ny))
            else:
                stack.pop()
            interactions += 1

        cells[0][0].open_wall(MazeWall.LEFT)
        cells[size-1][size-1].open_wall(MazeWall.RIGHT)

        print(interactions)
        return Maze(maze_cells_array=cells, size=size)

    def _find_unvisited_neighbors(self, x, y, size, visited):
        unvisited = []
        walls = list(MazeWall)
        random.shuffle(walls)
        for wall in walls:
            nx = x + wall.diff_x
            ny = y + wall.diff_y
            if nx < 0 or nx >= size or ny < 0 or ny >= size:
                continue
            if visited[nx][ny]:
                continue
            unvisited.append(wall)
        return unvisited

    def _create_initial_maze_walls(self, size):
        return [[MazeCell(x, y, walls=0) for y in range(size)] for x in range(size)]
