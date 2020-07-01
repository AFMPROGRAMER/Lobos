class Land:
    def __init__(self, tamX, tamY):
        self.tamX = tamX
        self.tamY = tamY
        self.creatures = []
        #Inicializamos el historico de pisadas para ver cuando el seto tiene que generarse
        self.fallow = [0] * tamX, [0] * tamY

    @property
    def tamX(self):
        return self.__tamX

    @tamX.setter
    def tamX(self, x):
        self.__tamX = x

    @property
    def tamY(self):
        return self.__tamY

    @tamY.setter
    def tamY(self, x):
        self.__tamY = x

    @property
    def creatures(self):
        return self.__creatures

    @creatures.setter
    def creatures(self, creatures):
        self.__creatures = creatures

    def addCreature(self, creature):
        return self.__creatures.append(creature)

    def killCreature(self, creature):
        return self.__creatures.pop(creature)
