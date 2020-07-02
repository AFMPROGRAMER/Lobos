from Entities.Posicion import Posicion


class SerVivo(Posicion):
    def __init__(self, x, y, color):
        Posicion.__init__(self, x, y)
        self.color = color
