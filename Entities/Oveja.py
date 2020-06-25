from Entities.SerVivo import SerVivo


class Oveja(SerVivo):

    def __init__(self, x, y):
        SerVivo.__init__(x, y, (255, 255, 255))
