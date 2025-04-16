import pygame
from model.enums.maze_wall import MazeWall
from model.maze import Maze

class MazeViewer:
    def __init__(self, maze: Maze, window_size: int = 600):
        self.maze = maze
        self.width = maze.size
        self.height = maze.size
        dimension = max(self.width, self.height)
        self.cell_size = window_size // dimension
        self.window_width = self.width * self.cell_size
        self.window_height = self.height * self.cell_size

        pygame.init()
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption("Maze")
        self.highlighted_cells = []
        self.wall_thickness = max(1, int(self.cell_size * 0.1))

    def draw(self):
        self.screen.fill((255, 255, 255))
        for row in self.maze.maze_cells_array:
            for cell in row:
                x = cell.x * self.cell_size
                y = cell.y * self.cell_size
                if not cell.is_open(MazeWall.TOP):
                    pygame.draw.line(self.screen, (0, 0, 0), (x, y), (x + self.cell_size, y), self.wall_thickness)
                if not cell.is_open(MazeWall.LEFT):
                    pygame.draw.line(self.screen, (0, 0, 0), (x, y), (x, y + self.cell_size), self.wall_thickness)
                if not cell.is_open(MazeWall.DOWN):
                    pygame.draw.line(self.screen, (0, 0, 0), (x, y + self.cell_size), (x + self.cell_size, y + self.cell_size), self.wall_thickness)
                if not cell.is_open(MazeWall.RIGHT):
                    pygame.draw.line(self.screen, (0, 0, 0), (x + self.cell_size, y), (x + self.cell_size, y + self.cell_size), self.wall_thickness)


        if self.highlighted_cells:
            total = len(self.highlighted_cells)
            gradient_count = total - 1
            for i, cell in enumerate(self.highlighted_cells):
                border = int(self.cell_size * 0.1)
                x = cell.x * self.cell_size
                y = cell.y * self.cell_size
                if i == total - 1:
                    color = (255, 0, 0)
                else:
                    fraction = i / gradient_count if gradient_count > 0 else 0
                    green_value = int(255 - fraction * (255 - 100))
                    color = (0, green_value, 0)
                rect = pygame.Rect(x + border, y + border, self.cell_size - 2 * border, self.cell_size - 2 * border)
                pygame.draw.rect(self.screen, color, rect)
        pygame.display.flip()

    def highlight_cells(self, cells):
        self.highlighted_cells = cells.copy()
        self.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

def show_maze(maze: Maze) -> MazeViewer:
    viewer = MazeViewer(maze)
    viewer.draw()
    return viewer
