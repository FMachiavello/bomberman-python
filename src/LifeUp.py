import powerUp


class LifeUp(powerUp.PowerUp):
    def __init__(self, posicion):
        super().__init__()
        self.type = "lifeup"
        self.posicion = posicion
        self.rect = None
        self.width = 36
        self.height = 36
        self.hitbox = (self.posicion[0], self.posicion[1], self.width, self.height)

# Setters

    def setPosicion(self, posicion):
        self.posicion = posicion

    def setRect(self, rect):
        self.rect = rect

# Getters

    def getPosition(self):
        return self.posicion

    def getRect(self):
        return self.rect

    def getHitbox(self):
        return self.hitbox

    def getType(self):
        return self.type
