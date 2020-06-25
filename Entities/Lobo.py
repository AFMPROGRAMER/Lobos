from Entities.SerVivo import SerVivo


class Lobo(SerVivo):

    def __init__(self, x,y):
        SerVivo.__init__(x, y, (128, 128, 128))
