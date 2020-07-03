import random
import config
import copy


class Creatures:

    def __init__(self, position, color=None, foodType=None):
        if color is None:
            color = [0, 0, 0]
        self.position = position
        self.color = color
        self.life = config.MAX_LIFE
        self.foodType = foodType

    # region getters
    @property
    def color(self):
        return self.color

    @property
    def life(self):
        return self.life

    @property
    def foodType(self):
        return self.foodType
    # endregion

    # region setters
    @color.setter
    def color(self, color):
        self.__color = color

    @life.setter
    def life(self, life):
        self.__life = life

    @foodType.setter
    def foodType(self, foodType):
        self.__foodType = foodType
    # endregion

    # region Move function
    def showPosition(self):
        return str(self.position.x) + ":" + str(self.position.y)

    def move(self, land):
        return self.__moveSimple(land)

    def __moveSimple(self, land):
        pos = None
        moveDo = random.randrange(8)

        if moveDo == 0:
            pos = self.position.moveN()
        elif moveDo == 1:
            pos = self.position.moveNE()
        elif moveDo == 2:
            pos = self.position.moveE()
        elif moveDo == 3:
            pos = self.position.moveES()
        elif moveDo == 4:
            pos = self.position.moveS()
        elif moveDo == 5:
            pos = self.position.moveSO()
        elif moveDo == 6:
            pos = self.position.moveO()
        elif moveDo == 7:
            pos = self.position.moveON()

        land.footPrint(pos.x, pos.y)

        return pos
    # endregion

    # region Life Functions
    def addLife(self):
        auxLife = self.life + 1
        if auxLife <= config.MAX_LIFE:
            self.life = auxLife
        return self.life

    def removeLife(self, land):
        self.life -= 1
        if self.life <= 0:
            land.killCreature(self)
        return self.life

    # endregion

    #  region Eat Functions
    def eat(self, land):
        res = False
        cratureList = None
        if self.foodType is not None:
            cratureList = land.getAllCreatureTypeInPosition(self.foodType, self.position)

        if cratureList is not None and len(cratureList) > 0:
            land.killCreature(cratureList[0])
            land.addCreature(self.createChild())
            res = True
        return res

    def createChild(self):
        child = copy.deepcopy(self)
        child.life = config.MAX_LIFE
    #  endregion
