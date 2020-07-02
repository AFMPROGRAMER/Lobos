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
    count = 0
    for creature in campo.creatures:
        count += 1

        # TODO: usar isinstance(a,TYPE) para saber de que ser vivo se trata
        if isinstance(creature, Hedge):
            print("Critura " + str(count) + ": Es un seto, en la posicion: " + creature.showPosition())
        elif isinstance(creature, Sheep):
            print("Critura " + str(count) + ":Es una oveja, en la posicion: " + creature.showPosition())
        elif isinstance(creature, Wolf):
            print("Critura " + str(count) + ":Es un lobo, en la posicion: " + creature.showPosition())
        else:
            print("Critura " + str(count) + ":No se que es, en la posicion: " + creature.showPosition())

