import numpy as np
import time

from Entities.hedge import Hedge
from Entities.land import Land
from Entities.position import Position
from Entities.sheep import Sheep
from Entities.wolf import Wolf

nxC = 80
nyC = 80

campo = Land(nxC, nyC)

#Inicializar los seres vivos en el tablero
seto1 = Hedge(Position(0, 0))
oveja1 = Sheep(Position(1, 1))
lobo1 = Wolf(Position(2, 2))
campo.addCreature(seto1)
campo.addCreature(oveja1)
campo.addCreature(lobo1)

#Bucle principal

while True:

    #TODO: Llamar al metodo pintar pantalla
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
