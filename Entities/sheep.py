from Entities.creatures import Creatures
from Entities.hedge import Hedge
from Entities.wolf import Wolf


class Sheep(Creatures):

    def __init__(self, position):
        super().__init__(position, [255, 255, 255])

    def move(self, land):
        # Buscamos cual es el seto mas cercano
        hedge = land.findNear(self.position, Hedge)
        pos = None
        # Calculo del movimiento idoneo
        # Comer
        if hedge is not None:
            if hedge.position.x < self.position.x and hedge.position.y < self.position.y:
                pos = self.position.moveON()
            elif hedge.position.x < self.position.x and hedge.position.y == self.position.y:
                pos = self.position.moveO()
            elif hedge.position.x < self.position.x and hedge.position.y > self.position.y:
                pos = self.position.moveSO()
            elif hedge.position.x > self.position.x and hedge.position.y < self.position.y:
                pos = self.position.moveNE()
            elif hedge.position.x > self.position.x and hedge.position.y == self.position.y:
                pos = self.position.moveE()
            elif hedge.position.x > self.position.x and hedge.position.y > self.position.y:
                pos = self.position.moveES()
            elif hedge.position.x == self.position.x and hedge.position.y < self.position.y:
                pos = self.position.moveS()
            elif hedge.position.x == self.position.x and hedge.position.y > self.position.y:
                pos = self.position.moveN()
            # Huir
            else:
                wolf = land.findNear(self.position, Wolf)
                if wolf is not None:
                    if wolf.position.x < self.position.x and wolf.position.y < self.position.y:
                        pos = self.position.moveES()
                    elif hedge.position.x < self.position.x and hedge.position.y == self.position.y:
                        pos = self.position.moveE()
                    elif hedge.position.x < self.position.x and hedge.position.y > self.position.y:
                        pos = self.position.moveNE()
                    elif hedge.position.x > self.position.x and hedge.position.y < self.position.y:
                        pos = self.position.moveSO()
                    elif hedge.position.x > self.position.x and hedge.position.y == self.position.y:
                        pos = self.position.moveO()
                    elif hedge.position.x > self.position.x and hedge.position.y > self.position.y:
                        pos = self.position.moveON()
                    elif hedge.position.x == self.position.x and hedge.position.y < self.position.y:
                        pos = self.position.moveN()
                    elif hedge.position.x == self.position.x and hedge.position.y > self.position.y:
                        pos = self.position.moveS()

        return pos
