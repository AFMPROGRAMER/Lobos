import time

import config
from Application.Utils.creatureFunctions import generateStartCreatures, generateHedge
from Entities.land import Land
from view.Viewservice import ViewService

nxC = config.MAX_X
nyC = config.MAX_Y

land = Land(nxC, nyC)
vs = ViewService(nxC, nyC)

#  Initialize start creature
generateStartCreatures(land)
vs.print_window(land)

iteration = 0
while iteration < config.MAX_ITERATIONS:

    # time.sleep(config.DELAY_TIME)
    vs.wait(config.DELAY_TIME)

    # move
    for creature in land.creatures:
        creature.removeLife(land)
        creature.move(land)

    # eat creatures
    for creature in land.creatures:
        creature.eat(land)

    # create hedge
    generateHedge(land)
    iteration += 1

    # refresh view
    vs.screen.fill(config.COLOR_FONT)
    vs.print_window(land)
