from Entities.position import Position


class Land:
    def __init__(self, tamX, tamY):
        self.tamX = tamX
        self.tamY = tamY
        self.creatures = []
        # Inicializamos el historico de pisadas para ver cuando el seto tiene que generarse
        self.fallow = [0] * tamX, [0] * tamY

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
        return self.__creatures.pop(creature)

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

    # region Hedge Functions
    def footPrint(self, x, y):
        res = False
        if x < self.tamX and y < self.tamY:
            self.fallow[x][y] = 0
            res = True
        return res

    # endregion

    # endregion

    # region Position Functions
    def getEmptySpace(self):
        posx = 0
        posy = 0
        find = False

        while (posx < self.tamX or posy < self.tamY) and not find:
            find = self.existCreature(posx, posy)
            if not find:
                posx += 1
                if posx >= self.tamX:
                    posy += 1
                    if posy < self.tamY:
                        posx = 0
        if not find:
            pos = None
        else:
            pos = Position(posx, posy)

        return pos
    # endregion