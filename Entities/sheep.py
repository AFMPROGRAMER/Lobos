from Entities.creatures import Creatures
from Entities.hedge import Hedge
from Entities.wolf import Wolf


class Sheep(Creatures):

    def __init__(self, position):
        super().__init__(position, [255, 255, 255])
