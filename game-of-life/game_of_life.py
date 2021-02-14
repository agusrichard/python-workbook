import pygame
import numpy as np

class GameofLife:
    def __init__(self, surface, width=1920, height=1080, scale=10, offset=1, active_color=(255, 255, 255), inactive_color=(50, 50, 50)):
        self.surface = surface
        self.width = width
        self.height = height
        self.scale = scale
        self.offset = offset
        self.active_color = active_color
        self.inactive_color = inactive_color

        self.columns = int(height / scale)
        self.rows = int(width / scale)

        self.grid = np.random.randint(0, 2, size=(self.rows, self.columns), dtype=bool)

    def run(self):
        """"Update and redraw the current grid state"""
        self.draw_grid()
        self.update_grid()

    def draw_grid(self):
        """Drawing the grid"""
        for row in range(self.rows):
            for col in range(self.columns):
                if self.grid[row, col]:
                    pygame.draw.rect(self.surface, self.active_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])
                else:
                    pygame.draw.rect(self.surface, self.inactive_color, [row * self.scale, col * self.scale, self.scale - self.offset, self.scale - self.offset])

    def update_grid(self):
        """Updating the grid based on Conway's game of life rules"""
        updated_grid = self.grid.copy()
        for row in range(updated_grid.shape[0]):
            for col in range(updated_grid.shape[1]):
                updated_grid[row, col] = self.update_cell(row, col)

        self.grid = updated_grid


    def update_cell(self, x, y):
        """Update single cell based on Conway's game of life rules"""
        current_state = self.grid[x, y]
        alive_neighbors = 0

        # Get to how many alive neighbors
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if i == 0 and j == 0:
                        continue
                    elif self.grid[x + i, y + j]:
                        alive_neighbors += 1
                except:
                    continue

        # Updating the cell's state
        if current_state and alive_neighbors < 2:                                       # dies as if by underpopulation
            return False
        elif current_state and (alive_neighbors == 2 or alive_neighbors == 3):          # lives to the next generation
            return True
        elif current_state and alive_neighbors > 3:                                     # dies as if by overpopulation
            return False
        elif ~current_state and alive_neighbors == 3:                                   # becomes alive as if by reproduction
            return True
        else:
            return current_state