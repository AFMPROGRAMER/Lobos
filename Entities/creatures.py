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
        return str(self.position.x) + ":" + str(self.position.y)

    def move(self):
        return self.position
