from Entities.hedge import Hedge
from Entities.wolf import Wolf


class Land:
    def __init__(self, tamX, tamY):
        self.tamX = tamX
        self.tamY = tamY
        self.creatures = []
        # Inicializamos el historico de pisadas para ver cuando el seto tiene que generarse
        self.fallow = [[0 for i in range(tamX)] for j in range(tamY)]

    # region getters
    @property
    def tamX(self):
        return self.__tamX

    @property
    def tamY(self):
        return self.__tamY

    @property
    def creatures(self):
        return self.__creatures

    @property
    def fallow(self):
        return self.__fallow

    # endregion

    # region setters
    @tamX.setter
    def tamX(self, x):
        self.__tamX = x

    @tamY.setter
    def tamY(self, x):
        self.__tamY = x

    @creatures.setter
    def creatures(self, creatures):
        self.__creatures = creatures

    @fallow.setter
    def fallow(self, fallow):
        self.__fallow = fallow

    # endregion

    # region Creature Functions
    def addCreature(self, creature):
        return self.__creatures.append(creature)

    def killCreature(self, creature):
        return self.__creatures.remove(creature)

    def existCreature(self, x, y):
        find = False
        limit = False
        cont = 0
        while not find and not limit:
            if cont >= len(self.creatures):
                limit = True
            else:
                if self.creatures[cont].position.x == x and self.creatures[cont].position.y == y:
                    find = True
                else:
                    cont += 1

        return find

    # region Creature Functions

    # region Hedge Functions
    def footPrint(self, x, y):
        res = False
        if x < self.tamX and y < self.tamY:
            self.fallow[x][y] = 0
            res = True
        return res

    def incrementFallow(self, x, y):
        res = False
        if x < self.tamX and y < self.tamY:
            self.fallow[x][y] += 1
            res = True
        return res

    # endregion

    def getAllCreatureType(self, creatureType):
        allCreatureType = []
        for creature in self.creatures:
            if isinstance(creature, creatureType):
                allCreatureType.append(creature)
        return allCreatureType

    def getAllHedge(self):
        return self.getAllCreatureType(Hedge)

    def getAllWolf(self):
        return self.getAllCreatureType(Wolf)

    def findNear(self, position, creatureType):
        near = None
        for creature in self.getAllCreatureType(creatureType):
            if near is None:
                near = creature.position
            if near.distance(position) > creature.position.distance(position):
                near = creature
        return near

    def getAllCreatureTypeInPosition(self, creatureType, position):
        listCreatureType = self.getAllCreatureType(creatureType)
        listAux = listCreatureType[:]
        count = 0
        for creature in listCreatureType:
            if (position is creature.position) | (creature.position.x != position.x & creature.position.y != position.y):
                listAux.pop()
            count += 1

        return listAux
    # endregion
