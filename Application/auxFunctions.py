from numpy import random
from Entities.hedge import Hedge
from Entities.sheep import Sheep
from Entities.wolf import Wolf


def generateStartCreatures(land):
    # Generamos 10 animales aleatorios con posciones aleatorias
    for i in range(0, 10):
        creatureType = random.randint(3)

        creature = None
        position = land.getEmptySpace()
        # Seto
        if position is not None:
            if creatureType == 0:
                creature = Hedge(position)
            # Oveja
            elif creatureType == 1:
                creature = Sheep(position)
            # Lobo
            elif creatureType == 2:
                creature = Wolf(position)
            else:
                creature = None
        if creature is not None:
            land.addCreature(creature)
