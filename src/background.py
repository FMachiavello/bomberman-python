import pygame
import game


class Background():
    def __init__(self, dimensions, game):
        pygame.init()
        pygame.display.set_caption("Bomberman")
        self.background = None
        self.screen = pygame.display.set_mode(dimensions)
        self.dimensions = dimensions
        self.bomberman = None
        self.game = game        # self.game = game.Game()
        pygame.key.set_repeat(50)

# Reload
    def reloadBackground(self, dimensions):
        for i in range(0, int((dimensions[0] / 37)) + 1):    # Creo Las Filas
            self.screen.blit(self.obstacle, (i * 37, 0))
            self.screen.blit(self.obstacle, (i * 37, dimensions[1] - 37))

        for i in range(0, int((dimensions[1] / 37)) + 1):   # Creo las columnas
            self.screen.blit(self.obstacle, (0, i * 37))
            self.screen.blit(self.obstacle, (dimensions[0] - 37, i * 37))

    def reloadObstacle(self, dimensions):
        for i in range(1, int((dimensions[0] / 37)) + 1):
            for z in range(1, int((dimensions[1]) / 37) + 1):
                self.screen.blit(self.obstacle, (i * 74, z * 74))

    def reloadBomberman(self):
        self.screen.blit(self.bomberman, self.game.getBombermanPosition())

# Loads
    def loadObstacle(self, path, pos):
        self.obstacle = pygame.image.load(path)
        self.screen.blit(self.obstacle, pos)

    def loadBackgroundImage(self, path):
        self.background = pygame.image.load(path)

    def loadBombermanImage(self, path, pos):
        self.bomberman = pygame.image.load(path)
        self.screen.blit(self.bomberman, pos)

# Etc
    def fillBlack(self):
        color = (0, 0, 0)
        self.screen.fill(color)
