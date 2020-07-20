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
    for key in land.creatures:
        for creature in land.creatures[key]:
            life = creature.removeLife(land)
            if life > 0:
                creature.move(land)

    # eat creatures
    for key in land.creatures:
        for creature in land.creatures[key]:
            creature.eat(land)

    # create hedge
    generateHedge(land)
    iteration += 1

    # refresh view
    vs.screen.fill(config.COLOR_FONT)
    vs.print_window(land)
