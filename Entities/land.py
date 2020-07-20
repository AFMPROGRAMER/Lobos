from Entities.hedge import Hedge
from Entities.sheep import Sheep
from Entities.wolf import Wolf


class Land:
    def __init__(self, tamX, tamY):
        self.tamX = tamX
        self.tamY = tamY
        self.creatures = self.intializeCreaturesLand(tamX, tamY)
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
        return self.__creatures[self.getKey(creature.position.x, creature.position.y)].append(creature)

    def killCreature(self, creature):
        return self.__creatures[self.getKey(creature.position.x, creature.position.y)].remove(creature)

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

    def getMostVisibleCreature(self, x, y):
        creature = None
        for key in self.creatures.keys():
            for auxCreature in self.creatures[key]:
                if auxCreature.position.x == x and auxCreature.position.y == y:
                    if creature is None or (
                            (isinstance(creature, Hedge) or isinstance(creature, Sheep)) and isinstance(auxCreature,
                                                                                                        Wolf)) or (
                            isinstance(creature, Hedge) and isinstance(auxCreature, Sheep)):
                        creature = auxCreature
        return creature

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
        listCreaturePosition = self.creatures[self.getKey(position.x,position.y)]

        listAux = listCreaturePosition[:]
        for creature in listCreaturePosition:
            if not isinstance(creature, creatureType):
                listAux.remove(creature)

        return listAux

    # endregion

    # region Dictionary Functions
    def getKey(self, x, y):
        return str(x) + "," + str(y)

    def intializeCreaturesLand(self, maxX, maxY):
        dictAux = {}
        for y in range(maxY):
            for x in range(maxX):
                dictAux.update({self.getKey(x, y): []})
        return dictAux

    def moveCreature(self, creature, newPosition):
        creatureOldPositionList = self.creatures[self.getKey(creature.position.x, creature.position.y)]
        creatureOldPositionList.remove(creature)
        creatureNewPositionList = self.creatures[self.getKey(newPosition.x, newPosition.y)]
        creatureNewPositionList.append(creature)

    # endregion
