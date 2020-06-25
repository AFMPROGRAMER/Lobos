from Entities import Campo


class Posicion(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_north(self):
        return [self.x % Campo.tamX, self.y + 1 % Campo.tamY]

    def move_northeast(self):
        return [self.x + 1 % Campo.tamX, self.y + 1 % Campo.tamY]

    def mover_east(self):
        return [self.x + 1 % Campo.tamX, self.y % Campo.tamY]

    def mover_southeast(self):
        return [self.x + 1 % Campo.tamX, self.y - 1 % Campo.tamY]

    def mover_south(self):
        return [self.x % Campo.tamX, self.y - 1 % Campo.tamY]

    def mover_southwest(self):
        return [self.x - 1 % Campo.tamX, self.y - 1 % Campo.tamY]

    def mover_west(self):
        return [self.x - 1 % Campo.tamX, self.y % Campo.tamY]

    def mover_northwest(self):
        return [self.x - 1 % Campo.tamX, self.y + 1 % Campo.tamY]
