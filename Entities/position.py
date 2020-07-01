from Entities.land import Land


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y

    def moveN(self, land):
        return [self.x % land.tamX, self.y + 1 % land.tamY]

    def moveNE(self, land):
        return [self.x + 1 % land.tamX, self.y + 1 % land.tamY]

    def moveE(self, land):
        return [self.x + 1 % land.tamX, self.y % land.tamY]

    def moveES(self, land):
        return [self.x + 1 % land.tamX, self.y - 1 % land.tamY]

    def moveS(self, land):
        return [self.x % land.tamX, self.y - 1 % land.tamY]

    def moveSO(self, land):
        return [self.x - 1 % land.tamX, self.y - 1 % land.tamY]

    def moveO(self, land):
        return [self.x - 1 % land.tamX, self.y % land.tamY]

    def moveON(self, land):
        return [self.x - 1 % land.tamX, self.y + 1 % land.tamY]
