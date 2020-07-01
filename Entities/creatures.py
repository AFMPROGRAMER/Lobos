from Entities.position import Position


class Creatures:

    def __init__(self, position, color=None):
        if color is None:
            color = [0, 0, 0]
        self.position = position
        self.color = color

    @property
    def color(self):
        return self.color

    @color.setter
    def color(self, color):
        self.__color = color

    def showPosition(self):
        return self.position
