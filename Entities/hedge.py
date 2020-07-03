from Entities.creatures import Creatures


class Hedge(Creatures):

    def __init__(self, position):
        super().__init__(position, [0, 255, 0])

    def move(self, land):
        return self.position
