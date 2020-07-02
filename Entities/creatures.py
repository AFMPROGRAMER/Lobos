from Entities.position import Position


class Creatures:

    def __init__(self, position, color=None):
        if color is None:
            color = [0, 0, 0]
        self.position = position
        self.color = color

    # region getters
    @property
    def color(self):
        return self.color
    # endregion

    # region setters
    @color.setter
    def color(self, color):
        self.__color = color
    # endregion

    def showPosition(self):
        return self.position

    def move(self):
        return self.position
