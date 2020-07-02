from Entities.creatures import Creatures


class Wolf(Creatures):

    def __init__(self, position):
        super().__init__(position, [125, 125, 125])

    def move(self):
        # TODO: Cambiar por funcion de movimiento real
        return self.position.moveN()
