import numpy as np
import time

from Application.auxFunctions import generateStartCreatures
from Entities.hedge import Hedge
from Entities.land import Land
from Entities.sheep import Sheep
from Entities.wolf import Wolf

nxC = 80
nyC = 80

campo = Land(nxC, nyC)

# Inicializar los seres vivos en el tablero
generateStartCreatures(campo)

# Bucle principal

while True:

    # TODO: Llamar al metodo pintar pantalla
    time.sleep(0.1)
    # Recorremos la lista de seres vivos
    for creature in campo.creatures:
        print(creature.showPosition())
        # TODO: usar isinstance(a,TYPE) para saber de que ser vivo se trata
        if isinstance(creature, Hedge):
            print("Es un seto")
        elif isinstance(creature, Sheep):
            print("Es una oveja")
        elif isinstance(creature, Wolf):
            print("Es un lobo")
        else:
            print("No se que es")

