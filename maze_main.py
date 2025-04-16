import time
from factory.maze_factory import MazeFactory
from solvers.impl.a_star_maze_solver import AStarMazeSolver
from maze_viewer import show_maze


def main():
    size = 50
    maze_factory = MazeFactory()
    maze = maze_factory.create_maze(size)
    solver = AStarMazeSolver()
    viewer = show_maze(maze)
    solver.solve(maze, viewer, 10)

    while True:
        viewer.check_events()
        time.sleep(0.01)

if __name__ == '__main__':
    main()
