from dynamicObject import DynamicObject
from bomb import Bomb
import pygame
import background


class Player(DynamicObject):
    def __init__(self):
        super().__init__()
        self.lifes = None
        self.speed = 3
        self.positionanterior = []
        # Colisiones
        self.x = self.position[0]
        self.y = self.position[1]
        self.width = 30
        self.height = 30
        self.hitbox = (self.x + 20, self.y, 30, 30)  # Dibujo un cuadrado
        self.direccion = None 

    def placeBomb(self, position, sprite):  # Coloca una bomba
        self.bomb = Bomb.createBomb(position, sprite)

    def createPlayer(self, lifes, speed):
        self.lifes = lifes
        self.speed = speed
        

# Movimiento

    def move(self, direccion, ventana):
        self.direccion = direccion
        for index in range(len(self.position)):
            print(self.position, "antes")
            self.position[index] = (self.position[index] + direccion[index] * (self.speed))
            print(self.position, "despues ")
            self.x = self.position[0]
            self.y = self.position[1]
            self.hitbox = (self.x, self.y, self.width, self.height)
            pygame.draw.rect(ventana, (255, 0, 0), self.hitbox, 2)
        if direccion == [0, -1]:
            self.direccion = "up"
        elif direccion == [0, 1]:
            self.direccion = "down"
        elif direccion == [1, 0]:
            self.direccion = "right"
        elif direccion == [-1, 0]:
            self.direccion = "left"

# Getters

    def getBombermanPosition(self):
        return self.position

    def getBombermanSpeed(self):
        print(self.speed)
        return self.speed

    def getBombermanDirection(self):
        return self.direccion

# Setters

    def setLifes(self, lifeAmmount):
        self.lifes = lifesAmmount

    def setPosition(self, aPosition):
        self.position = a_position

    def setSize(self, a_size):
        self.size = a_size

    def setSpeed(self, speedAmmount):
        self.speed += speedAmmount

    def setBombermanPosition(self, pos):
        self.position = pos
