from Entities.creatures import Creatures


class Sheep(Creatures):

    def __init__(self, position):
        super().__init__(position, [255, 255, 255])

    def move(self):
        # TODO: Cambiar por funcion de movimiento real
        return self.position.moveS()
