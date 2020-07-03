import time
import config

from Application.auxFunctions import generateStartCreatures, generateHedge
from Entities.hedge import Hedge
from Entities.land import Land
from Entities.sheep import Sheep
from Entities.wolf import Wolf

nxC = config.MAX_X
nyC = config.MAX_Y

campo = Land(nxC, nyC)

# Inicializar los seres vivos en el tablero
generateStartCreatures(campo)

# Bucle principal

while True:

    # TODO: Llamar al metodo pintar pantalla
    time.sleep(0.1)
    # Recorremos la lista de seres vivos
    count = 0
    # mover
    for creature in campo.creatures:
        count += 1

        if isinstance(creature, Hedge):
            # Los setos no se mueven
            print("Criatura " + str(count) + ": Es un seto, en la posicion: " + creature.showPosition())
        elif isinstance(creature, Sheep):

            print("Criatura " + str(count) + ":Es una oveja, en la posicion: " + creature.showPosition())
        elif isinstance(creature, Wolf):
            print("Criatura " + str(count) + ":Es un lobo, en la posicion: " + creature.showPosition())
        else:
            print("Criatura " + str(count) + ":No se que es, en la posicion: " + creature.showPosition())
        creature.removeLife(campo)
        creature.move(campo)

    count = 0
    # comer
    for creature in campo.creatures:
        count += 1
        if isinstance(creature, Hedge):
            # Los setos no comen
            print("Criatura " + str(count) + ": Es un seto, en la posicion: " + creature.showPosition())
        elif isinstance(creature, Sheep):
            print("Criatura " + str(count) + ":Es una oveja, en la posicion: " + creature.showPosition())
        elif isinstance(creature, Wolf):
            print("Criatura " + str(count) + ":Es un lobo, en la posicion: " + creature.showPosition())
        else:
            print("Criatura " + str(count) + ":No se que es, en la posicion: " + creature.showPosition())
        creature.eat(campo)

    # generamos setos
    generateHedge(campo)
