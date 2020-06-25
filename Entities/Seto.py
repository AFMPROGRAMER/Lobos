from Entities.SerVivo import SerVivo


class Seto(SerVivo):

    def __init__(self, x, y):
        SerVivo.__init__(x, y, (0, 255, 0))
