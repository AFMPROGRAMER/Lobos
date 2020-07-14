from Entities.creatures import Creatures
from Entities.sheep import Sheep


class Wolf(Creatures):

    def __init__(self, position):
        super().__init__(position, [125, 125, 125], Sheep)
