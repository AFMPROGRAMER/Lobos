from numpy import random

import config
from Entities.hedge import Hedge
from Entities.position import Position
from Entities.sheep import Sheep
from Entities.wolf import Wolf


def generateStartCreatures(land):
    # Generate random animal START_ANIMALS with random positions
    for i in range(0, config.START_ANIMALS):
        creatureType = random.randint(3)

        creature = None
        x = random.randint(0, config.MAX_X)
        y = random.randint(0, config.MAX_Y)
        position = Position(x, y)
        # Hedge
        if position is not None:
            if creatureType == 0:
                creature = Hedge(position)
            # Sheep
            elif creatureType == 1:
                creature = Sheep(position)
            # Wolf
            elif creatureType == 2:
                creature = Wolf(position)
            else:
                creature = None
        if creature is not None:
            land.addCreature(creature)


def generateHedge(land):
    x = 0
    for row in land.fallow:
        y = 0
        for position in row:
            position += 1
            land.incrementFallow(x, y)
            if position >= config.MAX_TIME_HEDGE:
                creature = Hedge(Position(x, y))
                land.addCreature(creature)
                land.footPrint(x, y)
            y += 1
        x += 1
