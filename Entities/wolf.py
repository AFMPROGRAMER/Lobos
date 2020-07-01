from Entities.creatures import Creatures


class Wolf(Creatures):

    def __init__(self, position):
        super().__init__( position, [125, 125, 125])

    def move(self):
        return self.position.moveN()
